"""
prompts.py

Contains all prompts used throughout
the project.
"""

CLAIM_EXTRACTION_PROMPT = """
You are an expert information extraction system.

Your task is to extract ONLY factual claims
from the advertisement below.

Rules:

1. Ignore promotional phrases.
2. Ignore emotional language.
3. Ignore opinions.
4. Ignore marketing slogans.
5. Extract only verifiable factual claims.
6. Keep claims concise.
7. Preserve wording as much as possible.
8. Do not invent information.

Return ONLY valid JSON.

Output format:

{
    "claims":[
        "...",
        "...",
        "..."
    ]
}

Advertisement:

{advertisement}
"""



AD_GENERATION_PROMPT = """
Generate a professional marketing advertisement using the product information below. The advertisement should primarily rely on the provided information and should sound natural and persuasive. If additional descriptive language is used, ensure it remains realistic and consistent with the product. Do not fabricate concrete specifications, certifications, numerical values, warranties, ingredients, dimensions, or technical features that are not provided. Return only the advertisement.
"""