# 📋 Mini Projeto - Gerenciador de Tarefas (Task Manager API)

Este projeto implementa um servidor de APIs (Backend) e um cliente consumidor (Consumer) para um sistema simples de Gerenciamento de Tarefas (To-Do List). O projeto foi desenvolvido como requisito do Terceiro Mini Projeto da disciplina Linguagem de Programação 2 na FATEC Rio Claro, com o tema **Consumo de APIs**.

## 🚀 Tecnologias Utilizadas

| Componente | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Servidor API (Backend)** | **Python** | Linguagem de programação principal. |
| | **FastAPI** | Framework de alto desempenho para criação da API. |
| | **Uvicorn** | Servidor ASGI para rodar a aplicação FastAPI. |
| | **Pydantic** | Utilizado para validação e modelagem de dados (schemas). |
| **Cliente (Consumer)** | **Python** | Linguagem de programação principal. |
| | **Requests** | Biblioteca para fazer chamadas HTTP (GET, POST, etc.) à API. |

---

## 📁 Estrutura do Projeto

A estrutura do projeto segue o modelo sugerido no documento do mini-projeto:

## Estrutura do Projeto

```bash
MINI_PROJETO-2-FATEC_2SEM/
├── server/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│
├── client/
│   ├── main.py
│
├── requirements.txt
└── README.md

```
---

## ⚙️ Instalação e Configuração

### Pré-requisitos

* [Python 3.8+](https://www.python.org/downloads/)

### Passos

1.  **Clone o Repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd mini_projeto_API
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    É crucial usar um ambiente virtual para gerenciar as dependências.
    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativação (Linux/macOS)
    source venv/bin/activate
    
    # Ativação (Windows - CMD)
    venv\Scripts\activate
    ```

3.  **Instale as Dependências:**
    Instale todas as bibliotecas listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃 Como Executar

Para testar o projeto, é necessário rodar o servidor e o cliente em terminais distintos.

### 1. Iniciar o Servidor FastAPI (Backend)

O servidor deve ser iniciado com o `uvicorn`. Mantenha este terminal aberto.

### Certifique-se de que o ambiente virtual está ativo

```bash
uvicorn server.app.main:app --reload
```

O servidor estará acessível em http://127.0.0.1:8000.

### 🔎 Documentação da API

Com o servidor rodando, você pode acessar a documentação interativa (Swagger UI) para testar os endpoints manualmente em:

    Swagger UI: http://127.0.0.1:8000/docs

### 2. Executar o Cliente (Consumer)

IMPORTANTE: O servidor (Passo 1) deve estar rodando para que as requisições do cliente funcionem.

Em um novo terminal, execute o script de demonstração do cliente:
```Bash
python client/main.py
```

O script demonstrará a sequência de chamadas CRUD (Criar, Listar, Atualizar, Deletar) e imprimirá os resultados no console.

🌐 Endpoints da API

| Método HTTP | Rota              | Descrição                                                  | Modelo de Entrada | Código de Status                    |
|--------------|------------------|------------------------------------------------------------|-------------------|-------------------------------------|
| **POST**     | `/tasks/`        | Cria uma nova tarefa.                                      | `TaskBase`        | `201 Created`                       |
| **GET**      | `/tasks/`        | Retorna a lista completa de tarefas.                       | N/A               | `200 OK`                            |
| **GET**      | `/tasks/{task_id}` | Retorna uma tarefa específica pelo ID.                     | N/A               | `200 OK` / `404 Not Found`          |
| **PATCH**    | `/tasks/{task_id}` | Atualiza campos específicos da tarefa (ex: `completed`).   | `TaskUpdate`      | `200 OK` / `404 Not Found`          |
| **DELETE**   | `/tasks/{task_id}` | Remove a tarefa do banco de dados.                         | N/A               | `204 No Content` / `404 Not Found`  |


🤝 Contribuições

Este projeto foi desenvolvido por:

[Bryan Juogiski Martini](https://github.com/Bryan-J-Martini)

[Rafael Henrique Martini Martins](https://github.com/RafaelHenriqueMM)