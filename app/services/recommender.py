# app/services/recommender.py

from torch.nn.functional import cosine_similarity
from itertools import product
import torch
from typing import List, Tuple
from transformers import AutoProcessor, AutoModelForZeroShotImageClassification

processor = AutoProcessor.from_pretrained("patrickjohncyh/fashion-clip")
model = AutoModelForZeroShotImageClassification.from_pretrained("patrickjohncyh/fashion-clip")


def get_text_embedding_dict(items: List[str]) -> dict:
    unique_items = list(set(items))
    inputs = processor(
        text=unique_items, return_tensors="pt", padding=True, truncation=True
    )
    with torch.no_grad():
        embeddings = model.get_text_features(**inputs)
    return dict(zip(unique_items, embeddings))


def score_outfit(embeddings: List[torch.Tensor], weights=(0.4, 0.4, 0.2)):
    sim12 = cosine_similarity(embeddings[0], embeddings[1], dim=0)
    sim13 = cosine_similarity(embeddings[0], embeddings[2], dim=0)
    sim23 = cosine_similarity(embeddings[1], embeddings[2], dim=0)
    return (weights[0] * sim12 + weights[1] * sim13 + weights[2] * sim23).item()


def generate_outfit_recommendations(
    shirts: List[str], 
    ties: List[str], 
    trousers: List[str], 
    top_n: int = 5
) -> List[Tuple[List[str], float]]:
    combos = list(product(shirts, ties, trousers))
    unique_texts = list(set(shirts + ties + trousers))
    embedding_dict = get_text_embedding_dict(unique_texts)

    scored_outfits = []
    for combo in combos:
        embeddings = [embedding_dict[item] for item in combo]
        score = score_outfit(embeddings)
        scored_outfits.append((list(combo), round(score, 3)))

    sorted_outfits = sorted(scored_outfits, key=lambda x: x[1], reverse=True)
    return sorted_outfits[:top_n]
