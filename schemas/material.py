from pydantic import BaseModel
from typing import Optional, List
from database.models.material import Material
from database.models.unidade import Unidade  

# Classe para definir como os dados de um novo material devem ser apresentados ao sistema
class MaterialSchema(BaseModel):
    """Define como um novo material a ser inserido deve ser representado."""
    nome: str = "Exemplo de Material"  
    quantidade: float = 10.0  
    custo_total: float = 100.0  
    unidade_id: int = 1

# Classe para buscar materiais com base no nome ou quantidade
#class MaterialBuscaSchema(BaseModel):
#    """Define como deve ser a estrutura que representa a busca de materiais."""
#    nome: Optional[str] = None  
#    quantidade_min: Optional[float] = None  
#    quantidade_max: Optional[float] = None  

# Classe para listar vários materiais como uma resposta da API
#class ListagemMateriaisSchema(BaseModel):
#    """Define como uma listagem de materiais será retornada."""
#    materiais: List[MaterialSchema]  

# Função que apresenta uma lista de materiais no formato necessário para retornar via API
def apresenta_materiais(materiais: List[Material]):
    """Retorna uma representação da lista de materiais seguindo o schema definido."""
    result = []
    for material in materiais:
        # Para cada material, montar um dicionário com as informações relevantes
        result.append({
            "id": material.id,
            "nome": material.nome,
            "quantidade": material.quantidade,
            "custo_total": material.custo_total,
            "unidade": material.unidade.nome if material.unidade else "Desconhecido"
        })
    return {"materiais": result}

# Classe para detalhar um material específico, incluindo todas as suas propriedades
class MaterialViewSchema(BaseModel):
    """Define como um material será retornado em detalhes, incluindo suas propriedades."""
    id: int = 1  
    nome: str = "Exemplo de Material" 
    quantidade: float = 10.0 
    custo_total: float = 100.0 
    unidade: str = "kg" 

# Classe para atualizar os dados de um material, onde os campos são opcionais
class MaterialUpdateSchema(BaseModel):
    """Define como um material deve ser atualizado."""
    nome: Optional[str] = "Novo nome do material"
    quantidade: Optional[float] = 15.0
    custo_total: Optional[float] = 120.0 
    unidade_id: Optional[int] = 1

# Função que apresenta um material no formato necessário para ser retornado via API
def apresenta_material(material: Material):
    """Retorna uma representação de um material seguindo o schema definido."""
    return {
        "id": material.id,
        "nome": material.nome,
        "quantidade": material.quantidade,
        "custo_total": material.custo_total,
        "unidade": material.unidade.nome if material.unidade else "Desconhecido",  # Utiliza a relação com unidade para obter o nome
    }
