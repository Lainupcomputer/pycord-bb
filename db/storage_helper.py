"""
Module for asynchronous key-value storage using SQLAlchemy ORM.

This module provides helper functions to store and retrieve simple textual or
numeric values in the `DataStorage` table. It is designed for lightweight
configuration handling, runtime flags, and general persistent state management
where a simple key-value storage mechanism is required.

The functions operate asynchronously and require an active SQLAlchemy
`AsyncSession` for all database operations.

Attributes:
    __version__ (str): Current module version.
    __author__ (str): Name of the module author.
    __license__ (str): License under which the module is distributed.
    __date__ (str): Creation or last-modified date of this module.
    __all__ (list[str]): Public API of this module; controls what gets exported
        when using `from module import *`.

Version:
    1.0.0.0
Author:
    Lainup
Date:
    2025-11-27
License:
    MIT License

Example:
    async with bot.db() as session:
        await set_value(session, "ticket_category_id", 123)
        value = await get_value(session, "ticket_category_id")
        await session.commit()
"""

__version__ = "1.0.0.0"
__author__ = "Lainup"
__license__ = "MIT"
__date__ = "2025-11-27"
__all__ = [
    "set_value",
    "get_value",
]


from .models import DataStorage
from sqlalchemy import select


async def set_value(session, key: str, value: str | int):
    """
    Store a value in the DataStorage table. If an entry with the given key already
    exists, its value will be updated; otherwise a new database entry will be created.

    **Example:**
        async with self.bot.db() as session:
            await set_value(session, "ticket_category_id", ticket_category.id)
            await session.commit()

    Parameters
    ----------
    session : AsyncSession
        An active SQLAlchemy session used to perform the database operation.
    key : str
        The unique key under which the value should be stored.
    value : str | int
        The value to store. It is internally saved as a string.

    Returns
    -------
    None
        This function does not return anything.
    """
    stmt = select(DataStorage).filter_by(key=key)
    result = await session.execute(stmt)
    entry = result.scalar_one_or_none()

    if entry:
        entry.data = str(value)  # update
    else:
        session.add(DataStorage(key=key, data=str(value)))


async def get_value(session, key: str) -> None | int | str:
    """
    Retrieve a value from the DataStorage table by its key. If no entry exists,
    ``None`` is returned.

    **Example:**
        async with self.bot.db() as session:
            value = await get_value(session, "ticket_category_id")
            await session.commit()

    Parameters
    ----------
    session : AsyncSession
        An active SQLAlchemy session used to perform the database operation.
    key : str
        The unique key whose stored value should be retrieved.

    Returns
    -------
    str | None
        The stored value as a string, or ``None`` if no entry exists.
    """
    stmt = select(DataStorage).filter_by(key=key)
    result = await session.execute(stmt)
    entry = result.scalar_one_or_none()

    if entry:
        return entry.data
    return None
