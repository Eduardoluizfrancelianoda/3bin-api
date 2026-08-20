# schemas.py
from pydantic import BaseModel, EmailStr


class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoResponse(ProdutoBase):
    id: int
    model_config = {"from_attributes": True}


class AlunoBase(BaseModel):
    nome: str
    matricula: str
    curso: str
    email: EmailStr


class AlunoCreate(AlunoBase):
    pass


class AlunoResponse(AlunoBase):
    id: int
    model_config = {"from_attributes": True}
