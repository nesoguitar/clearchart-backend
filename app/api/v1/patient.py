"""
GET /api/v1/patient/me — protected route (requires JWT).
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.patient import PatientProfile
from app.models.user import User
from app.schemas.patient import PatientMeResponse

router = APIRouter()


@router.get("/me", response_model=PatientMeResponse)
def get_my_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    profile = (
        db.query(PatientProfile).filter(PatientProfile.user_id == current_user.id).first()
    )
    # Defensive fallback: registration always creates a profile row, but if
    # one is somehow missing, don't 500 — just return null profile fields.
    return PatientMeResponse(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        created_at=current_user.created_at,
        age=profile.age if profile else None,
        gender=profile.gender if profile else None,
        conditions=profile.conditions if profile else None,
    )
