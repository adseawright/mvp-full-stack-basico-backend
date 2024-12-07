from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Material, Imposto, Unidade
import os

# Configuração do caminho do banco de dados
import os
db_path = "database/"
os.makedirs(db_path, exist_ok=True) 

db_url = f'sqlite:///{db_path}db.sqlite3'
engine = create_engine(db_url, echo=False)


# Criando a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Adicionando as unidades de medida ao banco de dados ao criar as tabelas
def create_tables():
    Base.metadata.create_all(bind=engine, checkfirst=True)  # evitaand recriar tabelas que já existem
    db = SessionLocal()
    try:
        # Verifica se as unidades já existem antes de inseri-las
        unidades_existentes = db.query(Unidade).first()
        if not unidades_existentes:
            unidades_padrao = ["Kg", "g", "L", "ml", "unidade"]
            for unidade in unidades_padrao:
                nova_unidade = Unidade(nome=unidade)
                db.add(nova_unidade)
            db.commit()
    except Exception as e:
        print(f"Erro ao adicionar unidades de medida: {e}")
    finally:
        db.close()

# Operações CRUD usando SQLAlchemy

# Função para criar um novo material
def create_material(nome, quantidade, custo_total, unidade_id):
    session = SessionLocal()
    try:
        novo_material = Material(
            nome=nome,
            quantidade=quantidade,
            custo_total=custo_total,
            unidade_id=unidade_id,
        )
        session.add(novo_material)
        session.commit()
    except Exception as e:
        print(f"Erro ao cadastrar material: {e}")
        session.rollback()
    finally:
        session.close()


# Função para obter todos os materiais cadastrados
def get_all_materials():
    session = SessionLocal()
    try:
        materiais = session.query(Material).all()
        return [{
            "id": material.id,
            "nome": material.nome,
            "quantidade": material.quantidade,
            "custo_total": material.custo_total,
            "unidade": material.unidade.nome if material.unidade else "N/A",  # Garantir que unidade não seja None
        } for material in materiais]
    except Exception as e:
        print(f"Erro ao listar materiais: {e}")
        return []
    finally:
        session.close()


# Função para atualizar um material existente
def update_material(id, nome, quantidade, custo_total, unidade_id):
    session = SessionLocal()
    try:
        material = session.query(Material).filter(Material.id == id).first()
        if material:
            material.nome = nome
            material.quantidade = quantidade
            material.custo_total = custo_total
            material.unidade_id = unidade_id
            session.commit()
    except Exception as e:
        print(f"Erro ao atualizar material: {e}")
        session.rollback()
    finally:
        session.close()


# Função para deletar um material
def delete_material(id):
    session = SessionLocal()
    try:
        material = session.query(Material).filter(Material.id == id).first()
        if material:
            session.delete(material)
            session.commit()
    except Exception as e:
        print(f"Erro ao deletar material: {e}")
        session.rollback()
    finally:
        session.close()

# Função para obter o valor do imposto
def get_tax():
    session = SessionLocal()
    try:
        imposto_entry = session.query(Imposto).filter(Imposto.chave == "imposto_total").first()
        return imposto_entry.valor if imposto_entry else 0.0
    except Exception as e:
        print(f"Erro ao obter imposto: {e}")
        return 0.0
    finally:
        session.close()

# Função para atualizar o valor do imposto
def update_tax(valor_imposto):
    session = SessionLocal()
    try:
        imposto_entry = session.query(Imposto).filter(Imposto.chave == "imposto_total").first()
        if imposto_entry:
            imposto_entry.valor = valor_imposto  # Atualizando o valor do imposto existente
        else:
            nova_imposto = Imposto(chave="imposto_total", valor=valor_imposto)  # Criando uma nova entrada para imposto
            session.add(nova_imposto)
        session.commit()
    except Exception as e:
        print(f"Erro ao atualizar imposto: {e}")
        session.rollback()
    finally:
        session.close()


# Função para obter todas as unidades de medida
def get_all_units():
    session = SessionLocal()
    try:
        unidades = session.query(Unidade).all()
        return [{"id": unidade.id, "nome": unidade.nome} for unidade in unidades]
    except Exception as e:
        print(f"Erro ao listar unidades: {e}")
        return []
    finally:
        session.close()

# Exemplo de execução da criação das tabelas
if __name__ == "__main__":
    create_tables()
