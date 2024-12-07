from sqlalchemy import Column, Integer, String, Float
from .base import Base

# Classe que representa a tabela 'impostos' no banco de dados
# Esta tabela armazena configurações gerais do sistema, como o valor do imposto, por exemplo.
class Imposto(Base):
    __tablename__ = 'impostos'

    id = Column(Integer, primary_key=True, index=True)
    chave = Column(String, unique=True, nullable=False)
    valor = Column(Float, nullable=False)
