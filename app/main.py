from fastapi import FastAPI
from app.database import Base, engine
from app.routers.games import router as games_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GameVault API",
    description="API para gerenciamento de jogos zerados",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "🎮 GameVault API está funcionando!!!"}

app.include_router(games_router)