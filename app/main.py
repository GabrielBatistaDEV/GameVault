from fastapi import FastAPI

app = FastAPI(
    title="GameVault API",
    description="API para gerenciamento de jogos zerados",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "🎮 GameVault API está funcionando!!!"}