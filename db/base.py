"""
SQLAlchemy declarative base module.

This module defines and exposes the global SQLAlchemy `Base` object used for
declarative ORM model definitions throughout the application. All ORM model
classes should inherit from this shared `Base` to ensure proper metadata
management and table creation.

Attributes:
    Base (DeclarativeBase): The root class for all ORM-mapped models.
    __version__ (str): Current module version.
    __author__ (str): Module author.
    __license__ (str): License identifier.
    __date__ (str): Creation or last modification date.
    __all__ (list[str]): Public API exports of this module.

Version:
    1.0.0.0
Author:
    Lainup
Date:
    2025-11-27
License:
    MIT License

Example:
    from .base import Base

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        username = Column(String, unique=True)
"""

__version__ = "1.0.0.0"
__author__ = "Lainup"
__license__ = "MIT"
__date__ = "2025-11-27"

__all__ = ["Base"]

from sqlalchemy.orm import declarative_base

Base = declarative_base()
