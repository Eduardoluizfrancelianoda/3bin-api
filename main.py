from fastapi import FastAPI
app = FastAPI()

@app.get ('/')
def ola_mundo():
    return{'mensagem':'minha primeira API em fastapi'}

@app.get ('/')
def clientes():
    return{'mensagem':'clientes'}