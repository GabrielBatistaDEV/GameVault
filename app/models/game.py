from sqlalchemy import Column, Date, Float, Integer, String, Text

from app.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text, nullable=True)
    nota = Column(Float, nullable=True)
    plataforma = Column(String(50), nullable=True)
    data_conclusao = Column(Date, nullable=True)