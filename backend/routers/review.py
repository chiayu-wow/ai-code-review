from fastapi import APIRouter
from models.review import ReviewRequest
from services.openai_service import review_code

router = APIRouter(prefix="/api/review", tags=["review"])

@router.post("/")
def review(request: ReviewRequest):
    result = review_code(request.code, request.language)
    return result