from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Paciente

Base.metadata.create_all(bind=engine)

app = FastAPI()

class TriagemRequest(BaseModel):
    nome: str
    idade: int
    sintomas: str

@app.post("/triagem")
def triagem(data: TriagemRequest):

    sintomas = data.sintomas.lower()

    classificacao = "verde"
    prioridade = 3
    encaminhamento = "consulta"

    if "dor no peito" in sintomas:
        classificacao = "vermelho"
        prioridade = 1
        encaminhamento = "emergência"

    db: Session = SessionLocal()

    paciente = Paciente(
        nome=data.nome,
        idade=data.idade,
        sintomas=data.sintomas,
        classificacao=classificacao,
        prioridade=prioridade,
        encaminhamento=encaminhamento
    )

    db.add(paciente)
    db.commit()

    return {
        "paciente": data.nome,
        "classificacao": classificacao,
        "prioridade": prioridade,
        "encaminhamento": encaminhamento
    }