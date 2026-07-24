# scripts/build_index.py
"""
🔨 بناء فهرس FAISS من knowledge_base
يشتغل تلقائياً عند بدء التطبيق لو الفهرس مش موجود
"""

import sys
import asyncio
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from core.config import settings
from database.docx_loader import DocxLoader
from database.embeddings import Embeddings
from database.faiss_loader import FAISSLoader
from utils.logger import logger


async def build_index():
    logger.info("🔨 Starting index build...")

    kb_path = settings.KNOWLEDGE_BASE_PATH
    if not kb_path.exists():
        logger.error(f"❌ knowledge_base not found: {kb_path}")
        return False

    # تحميل المستندات
    loader = DocxLoader()
    all_chunks = []

    for category_dir in kb_path.iterdir():
        if not category_dir.is_dir():
            continue
        for file_path in category_dir.glob("*.docx"):
            try:
                chunks = loader.load(str(file_path))
                for chunk in chunks:
                    if not isinstance(chunk, dict):
                        chunk = {"text": str(chunk), "metadata": {}}
                    chunk.setdefault("metadata", {})
                    chunk["metadata"]["category"] = category_dir.name
                    chunk["metadata"]["filename"] = file_path.name
                    all_chunks.append(chunk)
                logger.info(f"✅ Loaded: {file_path.name} ({len(chunks)} chunks)")
            except Exception as e:
                logger.error(f"❌ Error loading {file_path.name}: {e}")

    if not all_chunks:
        logger.error("❌ No chunks loaded!")
        return False

    logger.info(f"📄 Total chunks: {len(all_chunks)}")

    # توليد المتجهات
    embeddings_model = Embeddings(
        model_name=settings.EMBEDDING_MODEL,
        device=settings.EMBEDDING_DEVICE
    )

    texts = [c.get("text", "") for c in all_chunks]
    vectors = await embeddings_model.encode(texts)

    logger.info(f"🧬 Generated {len(vectors)} embeddings")

    # بناء الفهرس
    faiss_loader = FAISSLoader()
    faiss_loader.clear()

    for i, (chunk, vector) in enumerate(zip(all_chunks, vectors)):
        doc_id = f"doc_{i}_{chunk['metadata'].get('filename', 'unknown')}"
        faiss_loader.add_document(
            doc_id=doc_id,
            text=chunk.get("text", ""),
            embedding=vector,
            metadata=chunk.get("metadata", {})
        )

    # حفظ الفهرس
    success = faiss_loader.save()
    if success:
        logger.info(f"✅ Index built and saved! ({len(all_chunks)} documents)")
    else:
        logger.error("❌ Failed to save index!")

    return success


if __name__ == "__main__":
    asyncio.run(build_index())
