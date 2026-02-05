import functools
from typing import Callable, Awaitable


def with_db_session(func: Callable[..., Awaitable]):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        async with self.database() as session:
            return await func(self, session, *args, **kwargs)
    return wrapper
