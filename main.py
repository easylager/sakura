from fastapi import FastAPI

from src.api.v1.game_api import game_router

app = FastAPI()
app.include_router(game_router)
