"""
load_products.py
Responsible for loading the product dataset.
"""
import pandas as pd
def load_products(csv_path: str) -> pd.DataFrame:
    """
    Load products dataset from CSV.

    Parameters
    ----------
    csv_path : str
        Path to products.csv

    Returns
    -------
    pd.DataFrame
        Loaded dataframe
    """
    df = pd.read_csv(csv_path)
    print(f"[INFO] Loaded {len(df)} products.")
    return df

if __name__ == "__main__":

    df = load_products(
        "../../data/raw/products.csv"
    )

    print(df.head())