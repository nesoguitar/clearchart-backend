"""
SQLAlchemy declarative base. Models are imported here so Alembic's
autogenerate (and Base.metadata.create_all, if used) can see every table
regardless of import order elsewhere in the app.
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.user import User  # noqa: E402, F401
from app.models.patient import PatientProfile  # noqa: E402, F401
