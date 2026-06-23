"""
search_faiss.py

Query FAISS index.
"""

import numpy as np


def search_index(
    index,
    query_embedding: np.ndarray,
    k: int = 5
):
    """
    Search FAISS index.

    Parameters
    ----------
    index

    query_embedding

    k

    Returns
    -------
    distances
    indices
    """

    distances, indices = index.search(
        query_embedding.astype(
            np.float32
        ),
        k
    )

    return distances, indices