"""
PoE2 地面/螢幕掉落物即時 OCR 查價工具 - 主 UI 與懸浮 Overlay 介面
使用 Tkinter 打造優雅深色介面與全螢幕選區框。
"""
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import logging

from .price_db import PriceDatabase
from .ocr_engine import DropOcrEngine

logger = logging.getLogger(__name__)

class RegionSelector:
    """全螢幕滑鼠框選工具，讓使用者在畫面上拉出掃描區域。"""
    def __init__(self, callback):
        self.callback = callback
        self.root = tk.Toplevel()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)
        self.root.config(cursor="cross")

        self.canvas = tk.Canvas(self.root, cursor="cross", bg="gray")
        self.canvas.pack(fill="both", expand=True)

        self.start_x = None
        self.start_y = None
        self.rect_id = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline="red", width=3)

    def on_move_press(self, event):
        cur_x, cur_y = (event.x, event.y)
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = (event.x, event.y)
        x = min(self.start_x, end_x)
        y = min(self.start_y, end_y)
        w = abs(end_x - self.start_x)
        h = abs(end_y - self.start_y)
        self.root.destroy()
        if w > 10 and h > 10:
            self.callback((x, y, w, h))


class PriceOverlayWindow:
    """置頂透明懸浮視窗，顯示在框選區域邊緣，即時印出價格資訊。"""
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.9)
        self.root.config(bg="#111111")

        self.label = tk.Label(
            self.root,
            text="[PoE2 查價等待中]",
            font=("Microsoft JhengHei", 12, "bold"),
            fg="#00FFCD",
            bg="#111111",
            justify="left",
            padx=10,
            pady=6,
            relief="solid",
            bd=1
        )
        self.label.pack()
        self.root.withdraw()

    def update_text(self, text: str, x: int, y: int):
        if not text:
            self.root.withdraw()
            return

        self.label.config(text=text)
        self.root.geometry(f"+{x}+{y}")
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()


class MainDashboardApp:
    """主主機面板應用程式。"""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("PoE2 地面掉落物即時 OCR 查價工具")
        self.root.geometry("640x580")
        self.root.config(bg="#1A1D23")
        self.root.attributes("-topmost", True)

        self.price_db = PriceDatabase(league="Standard")
        self.ocr_engine = DropOcrEngine(price_db=self.price_db, lang="chi_tra+eng")
        self.overlay = PriceOverlayWindow()

        self.bbox = (400, 300, 300, 200)  # 預設範圍
        self.is_scanning = False
        self.scan_thread = None

        self.build_ui()

    def build_ui(self):
        # 標題區
        title_frame = tk.Frame(self.root, bg="#22262E", pady=10)
        title_frame.pack(fill="x")

        lbl_title = tk.Label(
            title_frame,
            text="💎 PoE2 地面掉落物即時 OCR 查價工具",
            font=("Microsoft JhengHei", 14, "bold"),
            fg="#4A9EFF",
            bg="#22262E"
        )
        lbl_title.pack()

        # 控制按鈕區
        ctrl_frame = tk.Frame(self.root, bg="#1A1D23", pady=10)
        ctrl_frame.pack(fill="x", padx=15)

        btn_select = tk.Button(
            ctrl_frame,
            text="🎯 選取螢幕掃描範圍",
            font=("Microsoft JhengHei", 11, "bold"),
            bg="#2A2E38",
            fg="#E8ECF1",
            activebackground="#4A9EFF",
            activeforeground="#FFFFFF",
            relief="flat",
            command=self.select_region,
            padx=10, pady=5
        )
        btn_select.grid(row=0, column=0, padx=5)

        self.btn_toggle = tk.Button(
            ctrl_frame,
            text="▶ 開始自動掃描",
            font=("Microsoft JhengHei", 11, "bold"),
            bg="#118C5C",
            fg="#FFFFFF",
            activebackground="#34D399",
            relief="flat",
            command=self.toggle_scanning,
            padx=10, pady=5
        )
        self.btn_toggle.grid(row=0, column=1, padx=5)

        btn_scan_once = tk.Button(
            ctrl_frame,
            text="⚡ 單次辨識測試",
            font=("Microsoft JhengHei", 11),
            bg="#2A2E38",
            fg="#E8ECF1",
            relief="flat",
            command=self.scan_once,
            padx=10, pady=5
        )
        btn_scan_once.grid(row=0, column=2, padx=5)

        # 區域與狀態顯示
        info_frame = tk.Frame(self.root, bg="#1A1D23")
        info_frame.pack(fill="x", padx=15, pady=5)

        self.lbl_bbox = tk.Label(
            info_frame,
            text=f"目前範圍: X={self.bbox[0]}, Y={self.bbox[1]}, W={self.bbox[2]}, H={self.bbox[3]}",
            font=("Consolas", 10),
            fg="#8A8F98",
            bg="#1A1D23"
        )
        self.lbl_bbox.pack(anchor="w")

        self.lbl_status = tk.Label(
            info_frame,
            text="狀態: 就緒 (請先選取螢幕上包含物品名稱/標籤的範圍)",
            font=("Microsoft JhengHei", 10),
            fg="#34D399",
            bg="#1A1D23"
        )
        self.lbl_status.pack(anchor="w", pady=2)

        # 輸出文字區（包含文字輸出面板，滿足視訊與記錄要求）
        log_label = tk.Label(
            self.root,
            text="📋 即時辨識與物價輸出文字區 (Real-time OCR & Price Output):",
            font=("Microsoft JhengHei", 11, "bold"),
            fg="#E8ECF1",
            bg="#1A1D23"
        )
        log_label.pack(anchor="w", padx=15, pady=(10, 2))

        log_frame = tk.Frame(self.root, bg="#111111")
        log_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.txt_log = tk.Text(
            log_frame,
            font=("Consolas", 11),
            bg="#111111",
            fg="#E8ECF1",
            insertbackground="white",
            relief="flat",
            wrap="word"
        )
        scrollbar = tk.Scrollbar(log_frame, command=self.txt_log.yview)
        self.txt_log.config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.txt_log.pack(side="left", fill="both", expand=True)

        self.log_message("系統初始化完成。請點擊「選取螢幕掃描範圍」來指定掉落物區域。")

    def log_message(self, msg: str):
        timestamp = time.strftime("%H:%M:%S")
        self.txt_log.insert(tk.END, f"[{timestamp}] {msg}\n")
        self.txt_log.see(tk.END)

    def select_region(self):
        self.root.iconify()  # 最小化主視窗方便選區
        time.sleep(0.2)
        RegionSelector(self.on_region_selected)

    def on_region_selected(self, bbox):
        self.bbox = bbox
        self.lbl_bbox.config(text=f"目前範圍: X={bbox[0]}, Y={bbox[1]}, W={bbox[2]}, H={bbox[3]}")
        self.root.deiconify()
        self.log_message(f"已更新掃描區域: X={bbox[0]}, Y={bbox[1]}, W={bbox[2]}, H={bbox[3]}")

    def scan_once(self):
        self.log_message("正在執行單次 OCR 掃描...")
        results = self.ocr_engine.scan_region(self.bbox)
        self.process_results(results)

    def process_results(self, results: list[dict]):
        if not results:
            self.log_message("⚠️ 區域內未識別出有效物品文字。")
            self.overlay.hide()
            return

        overlay_lines = []
        for item in results:
            raw = item["raw_text"]
            name = item["clean_name"]
            count = item["count"]
            pinfo = item["price_info"]

            if pinfo:
                chaos = pinfo["chaos"]
                unit = pinfo["unit"]
                zh_name = pinfo.get("zh") or name

                # 計算總價
                if unit == "divine":
                    total_price_str = f"{chaos * count:.2f} Div (單價 {chaos} Div)"
                else:
                    total_price_str = f"{chaos * count:.1f} Chaos"

                msg = f"✅ 辨識到: [{count}x {zh_name}] -> 估價: {total_price_str}"
                self.log_message(msg)
                overlay_lines.append(f"💰 {count}x {zh_name}: {total_price_str}")
            else:
                msg = f"❓ 辨識到: [{count}x {name}] (未找到對應物價資料)"
                self.log_message(msg)
                overlay_lines.append(f"❓ {count}x {name}: 未定價")

        if overlay_lines:
            # 將價格顯示在框選區域的右上方
            overlay_text = "\n".join(overlay_lines)
            target_x = self.bbox[0] + self.bbox[2] + 10
            target_y = self.bbox[1]
            self.overlay.update_text(overlay_text, target_x, target_y)

    def toggle_scanning(self):
        if self.is_scanning:
            self.is_scanning = False
            self.btn_toggle.config(text="▶ 開始自動掃描", bg="#118C5C")
            self.lbl_status.config(text="狀態: 已停止掃描", fg="#F87171")
            self.log_message("已停止自動掃描。")
            self.overlay.hide()
        else:
            self.is_scanning = True
            self.btn_toggle.config(text="⏹ 停止自動掃描", bg="#F87171")
            self.lbl_status.config(text="狀態: 自動掃描中 (每 0.8 秒掃描一次)...", fg="#34D399")
            self.log_message("開始自動掃描模式...")
            self.scan_thread = threading.Thread(target=self.scan_loop, daemon=True)
            self.scan_thread.start()

    def scan_loop(self):
        while self.is_scanning:
            try:
                results = self.ocr_engine.scan_region(self.bbox)
                self.root.after(0, self.process_results, results)
            except Exception as e:
                logger.error(f"掃描迴圈異常: {e}")
            time.sleep(0.8)

    def on_closing(self):
        self.is_scanning = False
        self.root.destroy()

def run_app():
    root = tk.Tk()
    app = MainDashboardApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    run_app()
