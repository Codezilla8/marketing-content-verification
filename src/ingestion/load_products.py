import pandas as pd

def load_products(csv_path):
    df = pd.read_csv(csv_path)
    return df