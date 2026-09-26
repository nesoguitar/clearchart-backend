"""
SQLAlchemy declarative base. Models are imported here so Alembic's
autogenerate (and Base.metadata.create_all, if used) can see every table
regardless of import order elsewhere in the app.
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

# Import models here for Alembic autogenerate
# Keep only the top-level package import to avoid circular imports
import app.models  # noqa: E402, F401
