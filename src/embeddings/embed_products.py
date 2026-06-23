"""
embed_products.py

Convert chunks into vector embeddings.
"""

from sentence_transformers import SentenceTransformer
import numpy as np


def embed_documents(
    chunks,
    model_name: str
) -> np.ndarray:
    """
    Convert chunks into embeddings.

    Parameters
    ----------
    chunks : list[dict]

    model_name : str

    Returns
    -------
    np.ndarray
    """

    print(
        f"[INFO] Loading model: {model_name}"
    )

    model = SentenceTransformer(
        model_name
    )

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    print(
        f"[INFO] Generated embeddings "
        f"for {len(texts)} chunks."
    )

    return embeddings