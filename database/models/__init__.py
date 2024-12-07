# Classe Material - define a tabela de materiais no banco de dados.
from .material import Material

# Classe Imposto - define a tabela de impostos no banco de dados.
from .imposto import Imposto

# Classe Base - A classe Base é a classe base do SQLAlchemy para todos os modelos.
# Engine - mecanismo de conexão ao banco de dados que será utilizado pelo SQLAlchemy.
from .base import Base, engine

# Classe Unidade - define a tabela de unidades no banco de dados.
from .unidade import Unidade
