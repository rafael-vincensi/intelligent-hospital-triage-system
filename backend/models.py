from sqlalchemy import Column, Integer, String
from database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    sintomas = Column(String)
    classificacao = Column(String)
    prioridade = Column(Integer)
    encaminhamento = Column(String)