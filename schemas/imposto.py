from pydantic import BaseModel

class ImpostoSchema(BaseModel):

    """
    Define como o valor do imposto deve ser representado.
    
    """    
    valor: float = 0.0 # Representa o valor do imposto com valor padrão 0.0, se não for fornecido.
