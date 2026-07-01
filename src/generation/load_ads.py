"""
load_ads.py

Responsible for loading AI-generated advertisements
from advertisements.json.
"""

import json
from pathlib import Path


def load_ads(json_path: str):
    """
    Load advertisements from a JSON file.

    Parameters
    ----------
    json_path : str
        Path to advertisements.json

    Returns
    -------
    list
        List of advertisement dictionaries.
    """

    json_path = Path(json_path)

    if not json_path.exists():
        raise FileNotFoundError(
            f"Advertisement file not found:\n{json_path}"
        )

    with open(
        json_path,
        "r",
        encoding="utf-8"
    ) as f:

        ads = json.load(f)

    if not isinstance(ads, list):
        raise ValueError(
            "advertisements.json must contain a list."
        )

    print(
        f"[INFO] Loaded {len(ads)} advertisements."
    )

    return ads


if __name__ == "__main__":

    ads = load_ads(
        "../../data/generated/advertisements.json"
    )

    print()

    print(ads[0])