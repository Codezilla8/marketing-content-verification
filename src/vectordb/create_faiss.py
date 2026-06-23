"""
create_faiss.py

Create and save FAISS indexes.
"""

import faiss
import numpy as np


def create_index(
    embeddings: np.ndarray
):
    """
    Create FAISS index.

    Parameters
    ----------
    embeddings : np.ndarray

    Returns
    -------
    faiss.Index
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings.astype(
            np.float32
        )
    )

    print(
        f"[INFO] Added "
        f"{index.ntotal} vectors "
        f"to FAISS."
    )

    return index


def save_index(
    index,
    path: str
):
    """
    Save index to disk.
    """

    faiss.write_index(
        index,
        path
    )

    print(
        f"[INFO] Saved index: "
        f"{path}"
    )


def load_index(
    path: str
):
    """
    Load index from disk.
    """

    index = faiss.read_index(
        path
    )

    print(
        f"[INFO] Loaded index: "
        f"{path}"
    )

    return index