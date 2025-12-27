# WS11 - Sistema CRUD de Produtos (Web Services)

## 📋 Descrição do Projeto
Este projeto consiste no desenvolvimento de um sistema completo de CRUD (Create, Read, Update, Delete) para gerenciamento de produtos através de uma API REST implementada em Python puro.

O sistema segue uma arquitetura em camadas (Entity, Service, Provider) e utiliza a biblioteca nativa `http.server` para o backend e `requests` para o cliente, demonstrando o funcionamento do protocolo HTTP sem o uso de frameworks de alto nível.

## 🏗️ Arquitetura e Estrutura
O projeto está organizado seguindo o padrão de separação de responsabilidades:

* **Entity (`produto.py`):** Define o modelo de dados.
* **Service (`produto_service.py`):** Contém a lógica de negócio e persistência em memória.
* **Provider (`ws_provider.py`):** Atua como servidor HTTP e Controller, expondo os endpoints.
* **Client (`ws_client_produto.py`):** Encapsula as chamadas HTTP para consumir a API.
* **Interface (`run.py`):** Menu interativo (CLI) para o usuário final.

### Estrutura de Diretórios
```text
WS11 - CRUD Produtos/
├── provider/                  # Backend (Servidor)
│   ├── produto.py             # Entidade Produto
│   ├── produto_service.py     # Regras de Negócio
│   └── ws_provider.py         # Servidor HTTP
├── client/                    # Frontend (Cliente)
│   ├── ws_client_produto.py   # Biblioteca de conexão
│   └── run.py                 # Interface CLI (Menu)
└── README.md                  # Documentação

```

## 📦 Modelo de Dados - Produto

A entidade `Produto` possui os seguintes atributos:

| Atributo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| **codigo** | `str` | Sim | Identificador único do produto |
| **nome** | `str` | Não | Nome descritivo do produto |
| **preco** | `float` | Não | Preço unitário |
| **quantidade** | `int` | Não | Quantidade em estoque |

## ⚙️ Requisitos e Instalação

### Pré-requisitos

* Python 3.x instalado.

### Instalação

O backend utiliza apenas bibliotecas nativas. Para o cliente, é necessário instalar a biblioteca `requests`:

```bash
pip install requests

```

## 🚀 Como Executar

O sistema funciona com dois terminais abertos simultaneamente (um para o servidor, outro para o cliente).

### Passo 1: Iniciar o Servidor (Backend)

1. Abra o terminal.
2. Navegue até a pasta `provider`.
3. Execute o servidor:
```bash
cd provider
python ws_provider.py

```


*O servidor iniciará em `http://127.0.0.1:8081*`

### Passo 2: Iniciar o Cliente (Frontend CLI)

1. Abra **outro** terminal.
2. Navegue até a pasta `client`.
3. Execute a interface:
```bash
cd client
python run.py

```


4. Utilize o menu interativo para gerenciar os produtos.

---

## 🌐 Documentação da API (Endpoints)

Todas as respostas são em formato JSON (`Content-Type: application/json`).

### 1. Listar Produtos

Retorna a lista de todos os produtos cadastrados.

* **Método:** `GET`
* **URL:** `/produtos`
* **Exemplo de Resposta:** `{"produtos": [{"codigo": "P01", ...}]}`

### 2. Buscar Produto

Busca um produto específico pelo código.

* **Método:** `GET`
* **URL:** `/produtos?codigo={codigo}`
* **Parâmetros:** `codigo` (Query String)
* **Exemplo de Resposta:** `{"produto": {...}}` ou `404 Not Found`

### 3. Criar Produto

Cadastra um novo produto.

* **Método:** `POST`
* **URL:** `/produtos`
* **Parâmetros (Query String):**
* `codigo` (Obrigatório)
* `nome`
* `preco`
* `quantidade`


* **Exemplo:** `/produtos?codigo=P01&nome=Mouse&preco=50`
* **Status Sucesso:** `201 Created`

### 4. Atualizar Produto

Atualiza os dados de um produto existente.

* **Método:** `PUT`
* **URL:** `/produtos`
* **Parâmetros (Query String):** `codigo` (Obrigatório) + campos a alterar.
* **Status Sucesso:** `200 OK`

### 5. Apagar Produto

Remove um produto do sistema.

* **Método:** `DELETE`
* **URL:** `/produtos`
* **Parâmetros (Query String):** `codigo` (Obrigatório).
* **Status Sucesso:** `200 OK`

---

## 🧪 Exemplos de Teste com cURL

Você pode testar a API diretamente pelo terminal usando o cURL (com o servidor rodando):

```bash
# 1. Criar um produto
curl -X POST "http://localhost:8081/produtos?codigo=TESTE01&nome=Teclado&preco=150.00&quantidade=10"

# 2. Listar todos
curl -X GET "http://localhost:8081/produtos"

# 3. Buscar específico
curl -X GET "http://localhost:8081/produtos?codigo=TESTE01"

# 4. Atualizar preço
curl -X PUT "http://localhost:8081/produtos?codigo=TESTE01&preco=120.00"

# 5. Apagar produto
curl -X DELETE "http://localhost:8081/produtos?codigo=TESTE01"

```

```

```
