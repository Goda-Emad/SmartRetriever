# database/text_loader.py
"""
📄 تحميل النصوص من ملفات TXT

يقرأ محتوى الملفات النصية العادية (.txt) بنفس واجهة DocxLoader
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import re

from utils.logger import logger


class TextLoader:
    """
    تحميل النصوص من ملفات .txt

    يدعم:
    - قراءة ملف واحد
    - قراءة كل ملفات .txt في مجلد
    - تنظيف النص المقروء
    """

    def __init__(self, clean_text: bool = True, remove_extra_spaces: bool = True, encoding: str = "utf-8"):
        self.clean_text = clean_text
        self.remove_extra_spaces = remove_extra_spaces
        self.encoding = encoding

        self.stats = {
            "total_loaded": 0,
            "total_failed": 0,
            "total_tokens": 0
        }

        logger.info("📄 TextLoader initialized")

    # ============================================================
    # الطرق الرئيسية
    # ============================================================

    def load_file(self, file_path: str) -> Optional[Dict[str, Any]]:
        try:
            path = Path(file_path)

            if not path.exists():
                logger.error(f"❌ File not found: {file_path}")
                return None

            if path.suffix.lower() != '.txt':
                logger.warning(f"⚠️ Not a TXT file: {file_path}")
                return None

            text = self._read_with_fallback_encoding(path)

            if not text:
                logger.warning(f"⚠️ No text extracted from: {file_path}")
                return None

            if self.clean_text:
                text = self._clean_extracted_text(text)

            self.stats["total_loaded"] += 1
            self.stats["total_tokens"] += len(text.split())

            return {
                "text": text,
                "metadata": {
                    "filename": path.name,
                    "file_path": str(path),
                    "file_size": path.stat().st_size,
                    "extension": path.suffix,
                    "category": self._guess_category(str(path)),
                },
                "file_path": str(path),
                "filename": path.name,
                "file_size": path.stat().st_size,
                "loaded_at": datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"❌ Error loading TXT {file_path}: {str(e)}")
            self.stats["total_failed"] += 1
            return None

    def load_directory(
        self,
        directory_path: str,
        recursive: bool = True,
        max_files: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        documents = []
        path = Path(directory_path)

        if not path.exists():
            logger.error(f"❌ Directory not found: {directory_path}")
            return []

        pattern = "**/*.txt" if recursive else "*.txt"
        files = list(path.glob(pattern))

        logger.info(f"📁 Found {len(files)} TXT files in {directory_path}")

        if max_files and len(files) > max_files:
            files = files[:max_files]
            logger.info(f"📁 Limiting to {max_files} files")

        for file_path in files:
            doc = self.load_file(str(file_path))
            if doc:
                documents.append(doc)

        logger.info(f"✅ Loaded {len(documents)} TXT documents")

        return documents

    # ============================================================
    # طرق مساعدة
    # ============================================================

    def _read_with_fallback_encoding(self, path: Path) -> str:
        """يحاول يقرأ بالـ encoding المحدد، ولو فشل يجرب utf-8-sig ثم latin-1"""
        encodings_to_try = [self.encoding, "utf-8-sig", "latin-1"]
        for enc in encodings_to_try:
            try:
                with open(path, "r", encoding=enc) as f:
                    return f.read()
            except (UnicodeDecodeError, LookupError):
                continue
        logger.error(f"❌ Could not decode file with any known encoding: {path}")
        return ""

    def _guess_category(self, file_path: str) -> str:
        filename = Path(file_path).name.lower()

        if 'contract' in filename or 'عقد' in filename:
            return 'contracts'
        elif 'policy' in filename or 'سياسة' in filename:
            return 'policies'
        elif 'quotation' in filename or 'عرض' in filename or 'سعر' in filename:
            return 'quotations'
        elif 'quality' in filename or 'جودة' in filename or 'تقرير' in filename:
            return 'quality_reports'
        else:
            return 'other'

    def _clean_extracted_text(self, text: str) -> str:
        if not text:
            return ""

        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)

        if self.remove_extra_spaces:
            text = re.sub(r'\s+', ' ', text)
            text = re.sub(r'\n\s*\n', '\n\n', text)

        text = re.sub(r'\n{3,}', '\n\n', text)
        text = text.strip()

        return text

    # ============================================================
    # إحصائيات
    # ============================================================

    def get_stats(self) -> Dict[str, Any]:
        return dict(self.stats)

    def reset_stats(self) -> None:
        self.stats = {
            "total_loaded": 0,
            "total_failed": 0,
            "total_tokens": 0
        }
        logger.info("🔄 TextLoader stats reset")

    def is_supported(self, file_path: str) -> bool:
        return Path(file_path).suffix.lower() == '.txt'
