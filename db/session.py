"""
Asynchronous database initialization and session management using SQLAlchemy.

This module configures an asynchronous SQLAlchemy engine and session factory
(`async_sessionmaker`) based on environment variables loaded from a `.env` file.
It ensures that all required database credentials are present and initializes
the database schema on startup.

The module is designed for applications that utilize an asynchronous MySQL
database connection via `aiomysql`. It exposes a session factory (`SessionLocal`)
and an initialization function (`init_db`) that creates all tables defined in
the SQLAlchemy ORM models.

Attributes:
    __version__ (str): Current module version.
    __author__ (str): Name of the module author.
    __license__ (str): License under which the module is distributed.
    __date__ (str): Creation or last modification date.
    __all__ (list[str]): Public API controlled export list.

Version:
    1.0.0.0
Author:
    Lainup
Date:
    2025-11-27
License:
    MIT License

Example:
    async def startup():
        await init_db()
        async with SessionLocal() as session:
            # use session here
            pass
"""

__version__ = "1.0.0.0"
__author__ = "Lainup"
__license__ = "MIT"
__date__ = "2025-11-27"
__all__ = [
    "engine",
    "init_db",
    "SessionLocal",
    "shutdown_db"
]
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .base import Base
from dotenv import load_dotenv
import os
import logging
logger = logging.getLogger("Database")

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

needed = [DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]

if any(x is None for x in needed):
    raise RuntimeError("Fehlende DB-Variablen in .env!")


DATABASE_URL = (
    f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=False,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)


async def init_db() -> None:
    """
    Initialize the database by creating all tables defined in the SQLAlchemy models.

    This operation is executed using the asynchronous engine and ensures that all
    ORM-mapped tables exist before the application starts using the database.

    Returns:
        None
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database started.")


async def shutdown_db() -> None:
    await engine.dispose()
    logger.info("Database closed.")
