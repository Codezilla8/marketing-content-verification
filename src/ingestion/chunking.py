# """
# chunking.py
# Convert products into retrievable chunks.
# """
# from typing import List
# def create_chunks(
#     df,
#     strategy: str = "product"
# ) -> List[dict]:
#     """
#     Create chunks from products.

#     Parameters
#     ----------
#     df : pd.DataFrame

#     strategy : str
#         "product"
#         "attribute"

#     Returns
#     -------
#     List[dict]
#     """
#     chunks = []

#     if strategy == "product":
#         for _, row in df.iterrows():
#             chunk_text = f"""
#             Product Name: {row['product_name']}
#             Brand: {row['brand']}
#             Category: {row['category']}
#             Subcategory: {row['subcategory']}

#             Description:
#             {row['product_description']}

#             Specifications:
#             {row['specifications']}
#             """

#             chunks.append({
#                 "product_id": row["product_id"],
#                 "chunk_type": "product",
#                 "text": chunk_text.strip()
#             })

#     elif strategy == "attribute":

#         for _, row in df.iterrows():

#             specs = str(
#                 row["specifications"]
#             ).split(";")

#             for spec in specs:

#                 spec = spec.strip()

#                 if not spec:
#                     continue

#                 chunk_text = f"""
#                 Product Name: {row['product_name']}
#                 Brand: {row['brand']}
#                 Category: {row['category']}

#                 {spec}
#                 """

#                 chunks.append({
#                     "product_id": row["product_id"],
#                     "chunk_type": "attribute",
#                     "text": chunk_text.strip()
#                 })

#     else:
#         raise ValueError(
#             "strategy must be "
#             "'product' or 'attribute'"
#         )
#     print(
#         f"[INFO] Created "
#         f"{len(chunks)} chunks "
#         f"using '{strategy}' strategy."
#     )
#     return chunks

"""
chunking.py

Convert products into retrievable chunks.
"""

from typing import List
import re


def create_chunks(
    df,
    strategy: str = "product"
) -> List[dict]:
    """
    Create chunks from products.

    Parameters
    ----------
    df : pd.DataFrame

    strategy : str
        "product"
        "attribute"

    Returns
    -------
    List[dict]
    """

    chunks = []

    # --------------------------------------------------
    # PRODUCT-LEVEL CHUNKING
    # --------------------------------------------------

    if strategy == "product":

        for _, row in df.iterrows():

            chunk_text = f"""
            Product Name: {row['product_name']}
            Brand: {row['brand']}
            Category: {row['category']}
            Price: ₹{row['price_inr']}

            Description:
            {row['product_description']}

            Specifications & Warranty:
            {row['specifications_and_warranty']}
            """

            chunks.append(
                {
                    "product_id": row["product_id"],
                    "product_name": row["product_name"],
                    "category": row["category"],
                    "chunk_type": "product",
                    "text": chunk_text.strip()
                }
            )

    # --------------------------------------------------
    # ATTRIBUTE-LEVEL CHUNKING
    # --------------------------------------------------

    elif strategy == "attribute":

        for _, row in df.iterrows():

            specs_text = str(
                row["specifications_and_warranty"]
            )

            # Split on both "|" and ";"
            specs = re.split(
                r"[|;]",
                specs_text
            )

            for spec in specs:

                spec = spec.strip()

                if not spec:
                    continue

                chunk_text = f"""
                Product Name: {row['product_name']}
                Brand: {row['brand']}
                Category: {row['category']}

                {spec}
                """

                chunks.append(
                    {
                        "product_id": row["product_id"],
                        "product_name": row["product_name"],
                        "category": row["category"],
                        "chunk_type": "attribute",
                        "text": chunk_text.strip()
                    }
                )

    else:

        raise ValueError(
            "strategy must be 'product' or 'attribute'"
        )

    print(
        f"[INFO] Created {len(chunks)} chunks "
        f"using '{strategy}' strategy."
    )

    return chunks