# app/schemas/request_response.py

from pydantic import BaseModel
from typing import List

class OutfitRequest(BaseModel):
    shirts: List[str]
    ties: List[str]
    trousers: List[str]
    top_n: int = 5

class OutfitRecommendation(BaseModel):
    outfit: List[str]
    score: float

class OutfitResponse(BaseModel):
    recommendations: List[OutfitRecommendation]
