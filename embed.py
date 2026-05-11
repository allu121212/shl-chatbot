import json
import numpy as np

from sentence_transformers import SentenceTransformer

print("Loading AI model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Loading catalog data...")

with open(
    "data/catalog.json",
    "r",
    encoding="utf-8"
) as f:

    catalog = json.load(f)

documents = []

for item in catalog:

    text = f"""
    Name: {item.get('name', '')}

    Description:
    {item.get('description', '')}
    """

    documents.append(text)

print("Creating embeddings...")

embeddings = model.encode(documents)

embeddings = np.array(
    embeddings,
    dtype="float32"
)

dimension = embeddings.shape[1]


index.add(embeddings)

faiss.write_index(
    index,
    "data/shl.index"
)

print("\nDONE")
print("Embeddings created:", len(documents))