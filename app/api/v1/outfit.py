# app/api/v1/router.py

from fastapi import APIRouter
from app.schemas.request_response import OutfitRequest, OutfitResponse, OutfitRecommendation
from app.services.recommender import generate_outfit_recommendations

router = APIRouter(prefix="/api/v1")

@router.post("/recommend", response_model=OutfitResponse)
def recommend_outfits(payload: OutfitRequest):
    results = generate_outfit_recommendations(
        shirts=payload.shirts,
        ties=payload.ties,
        trousers=payload.trousers,
        top_n=payload.top_n
    )

    return OutfitResponse(
        recommendations=[
            OutfitRecommendation(outfit=combo, score=score) for combo, score in results
        ]
    )
