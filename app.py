import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from
from database.db_manager import (
    create_material, 
    get_all_materials, 
    update_material, 
    delete_material, 
    create_tables, 
    get_all_units,
    update_tax,
    get_tax  
)
from schemas.imposto import ImpostoSchema  # Importando o ImpostoSchema para trabalhar com impostos

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)  # Permitir requisições de diferentes origens (CORS)

# Inicializar o Swagger para documentação da API
swagger = Swagger(app)

# Criar as tabelas necessárias no banco de dados se não existirem
create_tables()  

# Rota para cadastrar um novo material
@app.route('/cadastrar_material', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'Material cadastrado com sucesso'
        },
        500: {
            'description': 'Erro ao cadastrar material'
        }
    },
    'parameters': [
        {
            'name': 'material',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'quantidade': {'type': 'number'},
                    'custo_total': {'type': 'number'},
                    'unidade_id': {'type': 'number'}
                }
            }
        }
    ]
})
def cadastrar_material():
    try:

        data = request.get_json()
        nome = data.get('nome')
        quantidade = data.get('quantidade')
        custo_total = data.get('custo_total')
        unidade_id = data.get('unidade_id')

        # Verificar se todos os campos obrigatórios foram fornecidos
        if not all([nome, quantidade, custo_total, unidade_id]):
            return jsonify({"error": "Missing required fields"}), 400

        # Chamar a função para criar o material no banco de dados
        create_material(nome, quantidade, custo_total, unidade_id)
        return jsonify({"message": "Material cadastrado com sucesso"}), 201

    except Exception as e:
        print(f"Erro ao cadastrar material: {e}")  # Log para auxiliar na depuração
        return jsonify({"error": "Erro ao cadastrar material"}), 500


# Rota para listar todos os materiais
@app.route('/listar_materiais', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de materiais cadastrados',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'quantidade': {'type': 'number'},
                        'custo_total': {'type': 'number'},
                        'unidade': {'type': 'string'}
                    }
                }
            }
        },
        500: {
            'description': 'Erro ao listar materiais'
        }
    }
})
def listar_materiais():
    try:
        # Obter todos os materiais do banco de dados
        materiais = get_all_materials()
        serialized_materiais = [
            {
                'id': material.get('id'),
                'nome': material.get('nome'),
                'quantidade': material.get('quantidade'),
                'custo_total': material.get('custo_total'),
                'unidade': material.get('unidade'),
            } for material in materiais
        ]
        return jsonify(serialized_materiais), 200
    except Exception as e:
        return jsonify({'message': f'Erro ao listar materiais: {str(e)}'}), 500

# Rota para listar todas as unidades de medida
@app.route('/listar_unidades', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de unidades cadastradas',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'string'
                }
            }
        },
        500: {
            'description': 'Erro ao listar unidades'
        }
    }
})
def listar_unidades():
    try:
        # Obter todas as unidades disponíveis no banco de dados
        unidades = get_all_units()
        return jsonify(unidades), 200
    except Exception as e:
        return jsonify({'message': f'Erro ao listar unidades: {str(e)}'}), 500

# Rota para atualizar um material
@app.route('/atualizar_material/<int:id>', methods=['PUT'])
@swag_from({
    'responses': {
        200: {
            'description': 'Material atualizado com sucesso'
        },
        500: {
            'description': 'Erro ao atualizar material'
        }
    },
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        },
        {
            'name': 'material',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'quantidade': {'type': 'number'},
                    'custo_total': {'type': 'number'},
                    'unidade_id': {'type': 'number'}
                }
            }
        }
    ]
})
def atualizar_material_route(id):
    try:
        data = request.get_json()
        
        # Log para inspecionar os dados recebidos
        print("Dados recebidos para atualização:", data)
        
        nome = data.get('nome')
        quantidade = data.get('quantidade')
        custo_total = data.get('custo_total')
        unidade_id = data.get('unidade_id')

        # Verificar se todos os campos obrigatórios foram fornecidos
        if not all([nome, quantidade, custo_total, unidade_id]):
            return jsonify({"error": "Missing required fields"}), 400

        # Chamar a função para atualizar o material
        update_material(id, nome, quantidade, custo_total, unidade_id)
        return jsonify({'message': 'Material atualizado com sucesso!'}), 200
    except Exception as e:
        print(f"Erro ao atualizar material: {e}")
        return jsonify({'message': f'Erro ao atualizar material: {str(e)}'}), 500

# Rota para deletar um material
@app.route('/deletar_material/<int:id>', methods=['DELETE'])
@swag_from({
    'responses': {
        200: {
            'description': 'Material deletado com sucesso'
        },
        500: {
            'description': 'Erro ao deletar material'
        }
    },
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ]
})
def deletar_material(id):
    try:
        # Chamar a função para deletar o material pelo ID
        delete_material(id)
        return jsonify({'message': 'Material deletado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': f'Erro ao deletar material: {str(e)}'}), 500

# Rota para salvar o valor do imposto
@app.route('/salvar_imposto', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Imposto salvo com sucesso'
        },
        400: {
            'description': 'Erro ao validar imposto'
        },
        500: {
            'description': 'Erro ao salvar imposto'
        }
    },
    'parameters': [
        {
            'name': 'imposto',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'valor': {'type': 'number'}
                }
            }
        }
    ]
})
def salvar_imposto():
    try:
        # Extrair dados da requisição usando o ImpostoSchema
        data = request.get_json()
        imposto = ImpostoSchema(**data)

        # Validar valor do imposto (não pode ser negativo)
        if imposto.valor < 0:
            return jsonify({"error": "Valor inválido para o imposto"}), 400

        # Atualizar o valor do imposto no banco de dados
        update_tax(imposto.valor)  # Chamar a função que atualiza o valor do imposto

        return jsonify({"message": "Imposto salvo com sucesso"}), 200

    except Exception as e:
        print(f"Erro ao salvar imposto: {e}")
        return jsonify({"error": "Erro ao salvar imposto"}), 500

# Rota para obter o valor do imposto
@app.route('/obter_imposto', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Valor do imposto obtido com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'valor': {'type': 'number'}
                }
            }
        },
        500: {
            'description': 'Erro ao obter imposto'
        }
    }
})
def obter_imposto():
    try:
        # Obter o valor do imposto do banco de dados
        imposto = get_tax()
        return jsonify({"valor": imposto}), 200
    except Exception as e:
        print(f"Erro ao obter imposto: {e}")
        return jsonify({'message': 'Erro ao obter imposto'}), 500


# Executar a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
