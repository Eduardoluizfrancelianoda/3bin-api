# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB, AlunoDB
from schemas import (
    ProdutoCreate,
    ProdutoResponse,
    AlunoCreate,
    AlunoResponse,
)


Base.metadata.create_all(bind=engine)  # cria as tabelas, se ainda não existirem
app = FastAPI()

@app.get('/produtos', response_model=list[ProdutoResponse])

def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()

@app.post('/produtos', response_model=ProdutoResponse, status_code=201)

def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

from fastapi import HTTPException
# GET /produtos/{id} -> consulta um produto pelo id no banco
@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto
# DELETE /produtos/{id} -> remove um produto do banco
@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit()

# PUT /produtos/{id} -> atualiza um produto existente no banco
@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db:
Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade
    db.commit()
    db.refresh(produto)
    return produto


# --- Endpoints para Aluno ---
@app.get('/alunos', response_model=list[AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(AlunoDB).all()


@app.post('/alunos', response_model=AlunoResponse, status_code=201)
def criar_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    novo = AlunoDB(**aluno.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.get('/alunos/{aluno_id}', response_model=AlunoResponse)
def obter_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoDB).filter(AlunoDB.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail='Aluno não encontrado')
    return aluno


@app.put('/alunos/{aluno_id}', response_model=AlunoResponse)
def atualizar_aluno(aluno_id: int, dados: AlunoCreate, db: Session = Depends(get_db)):
    aluno = db.query(AlunoDB).filter(AlunoDB.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail='Aluno não encontrado')
    aluno.nome = dados.nome
    aluno.matricula = dados.matricula
    aluno.curso = dados.curso
    aluno.email = dados.email
    db.commit()
    db.refresh(aluno)
    return aluno


@app.delete('/alunos/{aluno_id}', status_code=204)
def remover_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoDB).filter(AlunoDB.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail='Aluno não encontrado')
    db.delete(aluno)
    db.commit()
