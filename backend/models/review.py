from pydantic import BaseModel

class ReviewRequest(BaseModel):
    code: str
    language: str = "auto"

class ReviewResponse(BaseModel):
    language: str
    review: str
    suggestions: list[str]