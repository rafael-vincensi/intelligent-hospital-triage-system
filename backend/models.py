from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)

    codigo = Column(String, unique=True)

    nome = Column(String)
    idade = Column(Integer)
    telefone = Column(String)

    sintomas = Column(String)

    classificacao = Column(String)
    prioridade = Column(Integer)
    encaminhamento = Column(String)
    justificativa = Column(String, default="")

    status = Column(String, default="Aguardando")

    observacoes = Column(String, default="")

    data_entrada = Column(
        DateTime,
        default=datetime.now
    )