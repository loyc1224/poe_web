"""
OCR 影像處理與文字辨識模組
專門針對 PoE2 地面/螢幕掉落物標籤（如 20x 點金石, 4x 改善之兆）進行前處理與文字提取。
"""
import re
import logging
import cv2
import numpy as np
import pytesseract
from PIL import Image
import mss

from .price_db import PriceDatabase

logger = logging.getLogger(__name__)

# 指定本機 Tesseract 執行檔路徑
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class DropOcrEngine:
    def __init__(self, price_db: PriceDatabase, lang: str = "chi_tra+eng"):
        self.price_db = price_db
        self.lang = lang
        self.sct = mss.mss()

    def capture_region(self, bbox: tuple[int, int, int, int]) -> np.ndarray:
        """從螢幕擷取指定範圍 (x, y, width, height)。"""
        x, y, w, h = bbox
        monitor = {"top": int(y), "left": int(x), "width": int(w), "height": int(h)}
        sct_img = self.sct.grab(monitor)
        img = np.array(sct_img)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    def preprocess_image(self, img: np.ndarray) -> np.ndarray:
        """圖像前處理：放大、灰階、對比拉伸與 Otsu 自適應二值化。"""
        # 放大 2 倍以提升小字體的 OCR 辨識率
        h, w = img.shape[:2]
        resized = cv2.resize(img, (w * 2, h * 2), interpolation=cv2.INTER_CUBIC)

        # 轉灰階
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        # 增加對比度 (CLAHE)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        contrast = clahe.apply(gray)

        # 二值化 - Otsu threshold
        _, thresh = cv2.threshold(contrast, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh

    def scan_region(self, bbox: tuple[int, int, int, int]) -> list[dict]:
        """
        截圖指定螢幕區域，執行 OCR 辨識並返回結果。
        回傳結構: [{ 'raw_text': str, 'clean_name': str, 'count': int, 'price_info': dict|None }]
        """
        try:
            raw_img = self.capture_region(bbox)
            processed_img = self.preprocess_image(raw_img)

            # 設定 Tesseract 參數: PSM 6 (假設單一文字區塊) 或 PSM 11 (Sparse text)
            custom_config = f"-l {self.lang} --psm 6"
            ocr_text = pytesseract.image_to_string(processed_img, config=custom_config)

            results = []
            lines = [line.strip() for line in ocr_text.splitlines() if line.strip()]

            for line in lines:
                parsed = self.parse_line(line)
                if parsed:
                    results.append(parsed)

            return results
        except Exception as e:
            logger.error(f"OCR 掃描錯誤: {e}")
            return []

    def parse_line(self, line: str) -> dict | None:
        """分析單行 OCR 文字，抽離數量與品名，並進行查價。"""
        # 清理多餘特殊字元，保留中文、英文、數字、x、X、空白與括號
        clean_line = re.sub(r"[^\w\s\(\)\-xX\u4e00-\u9fa5]", "", line).strip()
        if len(clean_line) < 2:
            return None

        # 提取數量模式: 如 "20x 點金石", "4x 改善之兆", "10x Orb of Alchemy"
        count = 1
        name = clean_line

        match = re.match(r"^(\d+)\s*[xX*]\s*(.+)$", clean_line)
        if match:
            try:
                count = int(match.group(1))
            except ValueError:
                count = 1
            name = match.group(2).strip()

        # 進一步清理品名開頭或結尾的數字雜訊
        name = re.sub(r"^\d+\s*", "", name).strip()

        if len(name) < 2:
            return None

        # 查詢價格
        price_info = self.price_db.get_price(name)

        return {
            "raw_text": line,
            "clean_name": name,
            "count": count,
            "price_info": price_info
        }
