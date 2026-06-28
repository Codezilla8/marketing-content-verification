# VeriMark
### Grounded Verification of AI-Generated Marketing Content Using Retrieval and Consistency Checking

> A modular Retrieval-Augmented Verification (RAV) framework that verifies factual claims made in AI-generated marketing advertisements using semantic retrieval, Natural Language Inference (NLI), and rule-based consistency checking.

---

# Overview

The rapid adoption of Large Language Models (LLMs) such as GPT, Gemini and Claude has enabled automatic generation of persuasive marketing advertisements. However, these advertisements may contain hallucinated, exaggerated or unsupported claims that can mislead consumers.

VeriMark is a research-oriented framework designed to automatically verify factual correctness in AI-generated marketing content.

Instead of trusting an advertisement, the system:

- extracts factual claims,
- retrieves supporting evidence from an authentic product knowledge base,
- verifies each claim against the retrieved evidence,
- assigns a confidence/risk score.

The framework is modular, allowing individual components to be replaced and evaluated independently.

---

# Objectives

- Build a structured product knowledge base.
- Generate and process AI-generated marketing advertisements.
- Extract factual claims from advertisements.
- Retrieve relevant evidence using semantic search.
- Verify claims using Natural Language Inference and rule-based methods.
- Produce interpretable verification reports.
- Compare different retrieval and verification strategies.

---

# Project Pipeline

```
                         Product Dataset
                                │
                                ▼
                     Data Preprocessing
                                │
                                ▼
                       Product Chunking
                                │
                                ▼
                     Sentence Embeddings
                                │
                                ▼
                         FAISS Index
────────────────────────────────────────────────────

                   AI Generated Advertisement
                                │
                                ▼
                      Claim Extraction
                                │
                                ▼
                    Claim Classification
                                │
                                ▼
                     Evidence Retrieval
                                │
                                ▼
              Natural Language Inference (NLI)
                                │
                                ▼
                  Numeric Consistency Checker
                                │
                                ▼
                        Risk Scoring
                                │
                                ▼
                    Verification Report
```

---

# Repository Structure

```
marketing-claim-verification/
│
├── data/
│   ├── raw/
│   │   └── products.csv
│   │
│   ├── generated/
│   │   ├── advertisements.json
│   │   ├── extracted_claims.json
│   │   ├── classified_claims.json
│   │   └── verification_results.json
│   │
│   └── evaluation/
│       └── ground_truth.json
│
├── src/
│   ├── ingestion/
│   │   ├── load_products.py
│   │   ├── preprocess.py
│   │   └── chunking.py
│   │
│   ├── embeddings/
│   │   └── embed_products.py
│   │
│   ├── vectordb/
│   │   ├── create_faiss.py
│   │   └── search_faiss.py
│   │
│   ├── generation/
│   │   └── generate_ads.py
│   │
│   ├── claims/
│   │   ├── extract_claims.py
│   │   └── classify_claims.py
│   │
│   ├── retrieval/
│   │   └── retrieve_evidence.py
│   │
│   ├── verification/
│   │   ├── nli_checker.py
│   │   ├── numeric_checker.py
│   │   └── risk_scoring.py
│   │
│   └── utils/
│       └── config.py
│
├── models/
│
├── notebooks/
│   └── experiments.ipynb
│
├── reports/
│   └── results.md
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
│
└── README.md
```

---

# Dataset

The knowledge base consists of curated product information collected from official brand websites and trusted e-commerce platforms.

Each row represents a unique product and serves as the ground-truth knowledge source during verification.

## Dataset Schema

| Column | Description |
|----------|-------------|
| Product_ID | Unique product identifier |
| Product Name | Product title |
| Category | Product category |
| Brand | Manufacturer / Brand |
| Source | Data source |
| Price (INR) | Selling price |
| Product Description | Natural language product description |
| Specifications & Warranty | Technical specifications, certifications and warranty information |
| Source URL | Original webpage |

---

## Dataset Statistics

Current Dataset

- Total Products : **100**
- Multiple Product Categories
- Product-level Chunks : **100**
- Attribute-level Chunks : **607**

The dataset spans multiple domains including:

- Electronics
- Sustainable Products
- Personal Care
- Home & Lifestyle
- Food & Beverage

making the verification framework category-independent.

---

# Generated Files

## advertisements.json

Stores advertisements generated manually or by LLMs.

```json
{
    "ad_id":"AD001",
    "product_id":"Elec-01",
    "product_name":"boAt Airdopes 141",
    "model":"manual",
    "advertisement":"..."
}
```

---

## extracted_claims.json

Stores extracted factual claims.

```json
{
    "claim_id":"C001",
    "ad_id":"AD001",
    "product_id":"Elec-01",
    "claim":"48 hours playback"
}
```

---

## classified_claims.json

Stores categorized claims.

```json
{
    "claim_id":"C001",
    "claim":"48 hours playback",
    "claim_type":"Battery"
}
```

---

## verification_results.json

Stores final verification output.

```json
{
    "claim_id":"C001",
    "claim":"48 hours playback",
    "retrieved_evidence":"Playback: 48 hrs",
    "verdict":"Supported",
    "risk_score":0.92
}
```

---

## ground_truth.json

Human-annotated labels used for evaluation.

```json
{
    "claim_id":"C001",
    "ground_truth":"Supported"
}
```

---

# Technologies Used

## Language

- Python

## Data Processing

- pandas
- NumPy

## Embedding Models

Current

- BAAI/bge-small-en-v1.5
- BAAI/bge-large-en-v1.5

Planned

- intfloat/e5-large-v2
- all-mpnet-base-v2

## Vector Database

- FAISS

Future

- BM25
- Hybrid Retrieval

## Verification Models

- BART MNLI
- DeBERTa MNLI
- RoBERTa MNLI

## Machine Learning

- scikit-learn
- PyTorch
- sentence-transformers
- transformers

---

# Experiments

The project evaluates multiple components independently.

## Stage A — Knowledge Base Construction

### Chunking Strategy

- Product Chunking
- Attribute Chunking

### Embedding Models

- BGE Small
- BGE Large

Future

- MPNet
- E5

---

## Stage B — Retrieval

- FAISS
- BM25 *(planned)*
- Hybrid Retrieval *(planned)*

Evaluation Metrics

- Top-1 Accuracy
- Top-3 Accuracy
- Top-5 Accuracy
- Recall@K
- Mean Reciprocal Rank (MRR)

---

## Stage C — Claim Extraction

Comparison of

- Manual Extraction
- LLM Extraction
- Open-source Models

---

## Stage D — Claim Classification

Comparison of

- Zero-shot Classification
- BART
- DeBERTa

---

## Stage E — Verification

Comparison of

- NLI Only
- NLI + Numeric Verification

---

## Stage F — Risk Scoring

Comparison of

- Similarity Only
- Similarity + NLI
- Similarity + NLI + Numeric

---

# Current Progress

## Completed

- Product dataset creation
- Product preprocessing
- Product chunking
- Semantic embeddings
- FAISS index creation
- FAISS search
- Chunking experiments
- Embedding experiments

## In Progress

- Advertisement generation
- Claim extraction
- Claim classification

## Upcoming

- Evidence retrieval
- NLI verification
- Numeric verification
- Risk scoring
- Streamlit interface

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd marketing-claim-verification
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the notebook

```bash
jupyter notebook notebooks/experiments.ipynb
```

---

# Future Improvements

- Automated advertisement generation using GPT, Gemini and Claude APIs
- Hybrid semantic + lexical retrieval
- Cross-Encoder reranking
- OCR-based advertisement verification
- Multimodal marketing content verification
- Explainable verification reports
- Knowledge graph integration

---

# Contributors

- **Jayant Bothra**
- **Khushi Wasnik** 

---

# Acknowledgements

This project is being developed as part of a research internship under the guidance of **Dr. Anupam Singh** (University of Glasgow), focusing on trustworthy AI systems for marketing content verification.
