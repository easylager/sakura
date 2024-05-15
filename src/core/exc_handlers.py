from contextlib import asynccontextmanager

from fastapi import HTTPException


@asynccontextmanager
async def exception_handler():
    try:
        yield
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
