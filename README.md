# Backend README

## Overview

Este documento fornece uma visão geral do backend do projeto **MVP FULL STACK BASICO**. O backend foi implementado utilizando **Flask**, e gerencia as rotas da API necessárias para a funcionalidade do projeto. Utiliza **SQLite** como banco de dados e a biblioteca **Flasgger** para gerar a documentação da API pelo Swagger.

## Estrutura do Projeto

O backend está organizado da seguinte maneira:

```
backend/
  |- app.py               # Código principal da aplicação Flask
  |- db_manager.py        # Funções relacionadas à interação com o banco de dados SQLite
  |- requirements.txt     # Dependências do Python necessárias para o backend
  |- README.md            # Este arquivo README
  |- docs/
      |- swagger.yaml     # Arquivo de configuração do Swagger para documentação da API
  |- database/
      |- db.sqlite3       # Banco de dados SQLite com as informações do projeto
      |- models/          # Modelos ORM usados pelo SQLAlchemy
  |- schemas/             # Schemas para validação e definição dos dados que passam pela API
      |- material.py      # Schema do Material
      |- imposto.py       # Schema do Imposto
```

### Principais Dependências

- **Flask**: Framework para a criação de APIs REST
- **Flask-Cors**: Para habilitar CORS na API e permitir que outras origens façam requisições
- **Flasgger**: Para gerar a documentação Swagger da API
- **SQLite**: Utilizado como banco de dados para armazenar informações dos materiais, unidades e configuração de impostos
- **SQLAlchemy**: ORM para interação com o banco de dados

## Executando o Backend

Siga as etapas a seguir para executar o backend no ambiente Windows:

1.**Entrar no diretorio do backend**
  No terminal, mude para o diretorio do backend:
  ```sh
  cd backend
  ```

2.**Criar o Ambiente Virtual**
   ```sh
   python -m venv env
   ```

3.**Ativar o ambiente Virtual**
  ```sh
  .\env\Scripts\Activate
  ```

4. **Instalar dependências**. 
   ```sh
   pip install -r requirements.txt
   ```

4. **Executar o Flask**:
   ```sh
   flask run --host 0.0.0.0 --port 5000
   ```

5. **Documentação da API**:
  
   A documentação Swagger pode ser acessada em:
   ```
   http://127.0.0.1:5000/apidocs
   ```
   Use esta interface para explorar e testar todas as rotas da API.

## Funcionalidades do Backend

### Rotas Implementadas

1. **Materiais**
   - **POST /cadastrar_material**: Cadastrar um novo material
   - **GET /listar_materiais**: Listar todos os materiais cadastrados
   - **PUT /atualizar_material/{id}**: Atualizar um material
   - **DELETE /deletar_material/{id}**: Deletar um material

2. **Impostos**
   - **POST /salvar_imposto**: Atualizar o valor do imposto.
   - **GET /obter_imposto**: Obter o valor atual do imposto.

3. **Unidades**
   - **GET /listar_unidades**: Listar todas as unidades de medida disponíveis.

### Banco de Dados

O banco de dados armazena os seguintes dados:

- **Materiais**: Informações sobre materiais cadastrados, incluindo nome, quantidade, custo total e ID da unidade de medida.
- **Impostos**: Armazena o valor do imposto pago (se for um item a parte na nota fiscal).
- **Unidades**: Lista de unidades de medida, como kg, litros, pacotes, etc.

### Flasgger e Swagger

O **Flasgger** gera a documentação da API, permitindo uma interação fácil com os endpoints através do navegador. A documentação está disponível na URL `/apidocs`.

## Exemplos de Requisição

Aqui estão exemplos de entradas para algumas das rotas principais:

### 1. Cadastrar Material (`POST /cadastrar_material`)

```json
{
  "nome": "Farinha de Trigo",
  "quantidade": 10,
  "custo_total": 50.00,
  "unidade_id": 1,
}
```

### 2. Atualizar Material (`PUT /atualizar_material/{id}`)

```json
{
  "nome": "Farinha de Trigo Integral",
  "quantidade": 8,
  "custo_total": 40.00,
  "unidade_id": 1,
}
```

### 3. Atualizar Imposto (`POST /salvar_imposto`)

```json
{
  "valor": 1.50
}
```

## Observações Importantes

- O backend deve estar sendo executado em conjunto com o frontend para proporcionar toda a funcionalidade do sistema.
- **CORS** foi configurado para permitir acesso de diferentes origens, facilitando a integração com o frontend.
- Certifique-se de que o banco de dados (`db.sqlite3`) está na pasta correta (`database/`) para evitar problemas de conexão.


## Estrutura dos Schemas

Os schemas do projeto são responsáveis pela validação e definição dos dados que transitam pela API. Eles estão localizados no diretório `schemas/`:

- **material.py**: Define os schemas relacionados aos materiais (MaterialSchema, MaterialUpdateSchema, etc.).
- **imposto.py**: Define o schema para a configuração de imposto.
