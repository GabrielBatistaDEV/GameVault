from datetime import date
from pydantic import BaseModel, Field

class GameCreate(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    descricao: str | None = None
    nota: float | None = Field(default=None, ge=0, le=10)
    plataforma: str | None = None
    data_conclusao: date | None = None

class GameResponse(GameCreate):
    id: int

    model_config = {
        "from_attributes": True
    }