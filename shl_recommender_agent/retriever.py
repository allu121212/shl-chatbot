import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


print("Loading retriever...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "data/shl.index"
)

with open(
    "data/catalog.json",
    "r",
    encoding="utf-8"
) as f:

    catalog = json.load(f)


def search_assessments(query, k=5):

    query_embedding = model.encode([query])

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:

        results.append(catalog[idx])

    return results