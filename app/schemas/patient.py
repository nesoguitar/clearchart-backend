from datetime import datetime

from pydantic import BaseModel, EmailStr


class PatientMeResponse(BaseModel):
    """
    Flattened user + patient-profile fields, as requested: one response
    object the Dashboard screen can render directly without reaching into
    a nested structure.
    """
    id: int
    email: EmailStr
    full_name: str
    created_at: datetime
    age: int | None
    gender: str | None
    conditions: str | None

    model_config = {"from_attributes": True}
