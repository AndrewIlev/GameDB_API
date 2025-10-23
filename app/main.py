from fastapi import FastAPI
from app.database import Base, engine
from app.routers import (
    player_router,
    guild_router,
    item_router,
    inventory_router,
    quest_router,
    skill_router,
    mathgame_router,
    achievement_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Підключаємо всі маршрутизатори
app.include_router(player_router.router)
app.include_router(guild_router.router)
app.include_router(item_router.router)
app.include_router(inventory_router.router)
app.include_router(quest_router.router)
app.include_router(skill_router.router)
app.include_router(mathgame_router.router)
app.include_router(achievement_router.router)