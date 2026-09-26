"""
GET /api/v1/health — public route, used for liveness checks and to
sanity-check the mobile app can reach the backend before wiring up auth.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}
