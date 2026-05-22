from pathlib import Path

import markdown
from flask import Flask, render_template

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"

CATEGORY_LABELS = {
    "strategy": "策略",
    "crafting": "做裝",
    "beetle": "甲蟲",
}


def get_strategy_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def render_markdown(text: str) -> str:
    text = text.replace("](./", "](/static/images/")
    return markdown.markdown(text, extensions=["extra", "tables", "sane_lists"])


def make_category_label(name: str) -> str:
    return CATEGORY_LABELS.get(name, name.replace("-", " ").replace("_", " ").title())


def build_summary(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            return stripped[2:].strip()
    return "尚未提供摘要。"


def load_categories() -> list[dict[str, object]]:
    if not CONTENT_DIR.exists():
        return []

    categories: list[dict[str, object]] = []
    for category_dir in sorted(path for path in CONTENT_DIR.iterdir() if path.is_dir()):
        documents: list[dict[str, str]] = []
        for file_path in sorted(category_dir.glob("*.md")):
            text = file_path.read_text(encoding="utf-8")
            title = get_strategy_title(text, file_path.stem)
            documents.append(
                {
                    "id": f"{category_dir.name}-{file_path.stem}",
                    "title": title,
                    "filename": file_path.name,
                    "category": category_dir.name,
                    "summary": build_summary(text),
                    "html": render_markdown(text),
                }
            )

        categories.append(
            {
                "id": category_dir.name,
                "label": make_category_label(category_dir.name),
                "count": len(documents),
                "documents": documents,
            }
        )

    return categories


@app.route("/")
def home():
    categories = load_categories()
    return render_template("index.html", categories=categories)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
