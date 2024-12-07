from sqlalchemy import Column, Integer, String
from .base import Base

# Classe que representa a tabela 'unidades' no banco de dados
# Essa tabela armazena as unidades de medida relacionadas aos materiais usados (como "Kg", "L", etc.).
class Unidade(Base):
    # Nome da tabela no banco de dados
    __tablename__ = 'unidades'

    # Definição das colunas da tabela
    id = Column(Integer, primary_key=True, index=True)  
    nome = Column(String, unique=True, nullable=False)  
