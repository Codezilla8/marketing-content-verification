# """
# preprocess.py
# Responsible for cleaning and normalizing
# the products dataset.
# """
# import pandas as pd
# import re

# def clean_text(text: str) -> str:
#     """
#     Clean a single text field.

#     Parameters
#     ----------
#     text : str

#     Returns
#     -------
#     str
#     """
#     if pd.isna(text):
#         return ""
#     text = str(text)
#     # Remove extra spaces
#     text = re.sub(r"\s+", " ", text)
#     # Remove spaces before punctuation
#     text = re.sub(r"\s*:\s*", ": ", text)

#     return text.strip()


# def preprocess_dataframe(
#     df: pd.DataFrame
# ) -> pd.DataFrame:
#     """
#     Clean entire dataframe.

#     Parameters
#     ----------
#     df : pd.DataFrame

#     Returns
#     -------
#     pd.DataFrame
#     """
#     df = df.copy()
#     text_columns = [
#         "product_name",
#         "brand",
#         "product_description",
#         "specifications",
#         "source",
#         "source_url",
#         "category",
#         "subcategory"
#     ]
#     for column in text_columns:

#         if column in df.columns:

#             df[column] = df[column].apply(
#                 clean_text
#             )
#     return df

# if __name__ == "__main__":
#     from load_products import load_products
#     df = load_products(
#         "../../data/raw/products.csv"
#     )
#     cleaned_df = preprocess_dataframe(df)
#     print(cleaned_df.head())

"""
preprocess.py
Responsible for cleaning and normalizing
the products dataset.
"""

import pandas as pd
import re

def clean_text(text: str) -> str:
    """
    Clean a single text field.
    """

    if pd.isna(text):
        return ""

    text = str(text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Normalize colon spacing
    text = re.sub(r"\s*:\s*", ": ", text)

    return text.strip()


def normalize_column_names(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Convert CSV column names into a
    consistent snake_case format.
    """

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("&", "and", regex=False)
    )

    return df


def preprocess_dataframe(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Clean and normalize entire dataframe.
    """

    df = normalize_column_names(df)

    text_columns = [
        "product_id",
        "product_name",
        "category",
        "brand",
        "source",
        "product_description",
        "specifications_and_warranty",
        "source_url"
    ]

    for column in text_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .fillna("")
                .apply(clean_text)
            )

    return df


if __name__ == "__main__":

    from load_products import load_products

    df = load_products(
        "../../data/raw/products.csv"
    )

    cleaned_df = preprocess_dataframe(df)

    print("\nColumns:\n")
    print(cleaned_df.columns.tolist())

    print("\nFirst Row:\n")
    print(cleaned_df.head(1))