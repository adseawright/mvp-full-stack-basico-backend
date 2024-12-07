from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Cria uma classe Base para ser usada como base para os modelos ORM
Base = declarative_base()

# Define o URL do banco de dados
DATABASE_URL = 'sqlite:///database/db.sqlite3'

# Cria o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL, echo=True)
