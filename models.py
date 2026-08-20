# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base
class ProdutoDB(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)


class AlunoDB(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    matricula = Column(String(50), unique=True, nullable=False)
    curso = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)