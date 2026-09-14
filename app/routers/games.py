from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.game import Game
from app.schemas.game import GameCreate, GameResponse

router = APIRouter(
    prefix="/games",
    tags=["Games"],
)


@router.post("/", response_model=GameResponse)
def criar_game(game: GameCreate, db: Session = Depends(get_db)):
    novo_game = Game(**game.model_dump())

    db.add(novo_game)
    db.commit()
    db.refresh(novo_game)

    return novo_game


@router.get("/", response_model=list[GameResponse])
def listar_games(db: Session = Depends(get_db)):
    return db.query(Game).all()


@router.get("/{game_id}", response_model=GameResponse)
def buscar_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()

    if not game:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado",
        )

    return game


@router.put("/{game_id}", response_model=GameResponse)
def atualizar_game(
    game_id: int,
    game_data: GameCreate,
    db: Session = Depends(get_db),
):
    game = db.query(Game).filter(Game.id == game_id).first()

    if not game:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado",
        )

    for campo, valor in game_data.model_dump().items():
        setattr(game, campo, valor)

    db.commit()
    db.refresh(game)

    return game


@router.delete("/{game_id}")
def deletar_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()

    if not game:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado",
        )

    db.delete(game)
    db.commit()

    return {
        "message": "Jogo excluído com sucesso",
    }