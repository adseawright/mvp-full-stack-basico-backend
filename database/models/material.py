from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.models.base import Base
from database.models.unidade import Unidade

# Classe que representa a tabela 'materiais' no banco de dados
class Material(Base):
    __tablename__ = 'materiais'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Float, nullable=False)
    custo_total = Column(Float, nullable=False)
    unidade_id = Column(Integer, ForeignKey('unidades.id'), nullable=False)

    # Relacionamento com a classe Unidade para obter informações da unidade de medida do material
    unidade = relationship("Unidade")
