from schemas.material import (
    MaterialSchema,  # Classe que define a estrutura do material para a inserção.
    MaterialUpdateSchema,  # Classe que define a estrutura dos dados que podem ser atualizados de um material.
    apresenta_materiais  # Função que transforma uma lista de objetos Material em um dicionário pronto para retornar via API.
    # ListagemMateriaisSchema,  # Classe que define como uma listagem de materiais será representada.
    # MaterialBuscaSchema,  # Classe que define a estrutura usada para buscar materiais. Comentada pois não está sendo utilizada no momento.
)

from schemas.imposto import ImpostoSchema  # Classe que define como representar os dados do imposto.
