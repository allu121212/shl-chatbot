import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


print("Loading retriever...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2",device="cpu"
)

def search_assessments(query):
    assessments = [
        {"name": "Java Developer Test", "url": "https://www.shl.com/java"},
        {"name": "Python Developer Test", "url": "https://www.shl.com/python"},
        {"name": "Frontend Developer Test", "url": "https://www.shl.com/frontend"},
        {"name": "Cognitive Ability Test (GSA)", "url": "https://www.shl.com/gsa"},
        {"name": "Personality Assessment (OPQ)", "url": "https://www.shl.com/opq"}
    ]

    query_words = set(query.lower().split())

    scored_results = []

    for item in assessments:
        name_words = set(item["name"].lower().split())

        # simple similarity score
        score = len(query_words & name_words)

        if score > 0:
            scored_results.append((score, item))

    scored_results.sort(reverse=True, key=lambda x: x[0])

    results = [item for _, item in scored_results]

    if not results:
        results = assessments

    return results