# 📦 Projeto FastAPI - Aula 08 & 09

Este projeto foi desenvolvido como parte do material de estudo das aulas 08 e 09, com o objetivo de aplicar conceitos básicos e intermediários de APIs REST usando FastAPI, testes automatizados com Pytest, gerenciamento de dependências com Poetry e formatação com Ruff.

---

## 🚀 Funcionalidades

- Criação de uma API REST com FastAPI.
- Endpoint `/novo` que retorna uma mensagem JSON.
- Documentação interativa com Swagger UI e Redoc.
- Testes automatizados com Pytest.
- Validação de dados com Pydantic.
- Organização em estrutura `src/` para melhor manutenção.
- Debugging com breakpoint e terminal interativo.
- Linters e formatação automática de código com Ruff.
- Gerenciamento de pacotes com Poetry e Pyenv.

---

## 📂 Estrutura do Projeto

```bash
aula08/
│
├── src/
│   └── aula08/
│       ├── app.py           # Arquivo principal com a API
│       ├── schema.py        # Modelos de dados com Pydantic
│       └── ...
│
├── tests/
│   └── test_app.py          # Testes para a API
│
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## 🧪 Executando os testes

Usamos `taskipy` para facilitar os comandos de teste.

```bash
poetry shell
task test
```

Ou, se preferir:

```bash
poetry run task test
```

---

## 🧰 Ferramentas utilizadas

### 📌 Linguagem

- **Python 3.13.3**

### ⚙️ Ferramentas

| Ferramenta    | Descrição |
|---------------|-----------|
| **FastAPI**   | Framework web rápido para criação de APIs REST. |
| **Uvicorn**   | Servidor ASGI para executar a aplicação FastAPI. |
| **Pytest**    | Framework de testes para Python. |
| **Taskipy**   | Ferramenta para definir e rodar tarefas automatizadas com `task`. |
| **Poetry**    | Gerenciador de dependências e ambientes virtuais. |
| **Pyenv**     | Gerenciador de versões do Python (instalação da 3.13.3). |
| **Pydantic**  | Validação de dados e definição de esquemas para a API. |
| **Swagger**   | Interface de documentação interativa gerada automaticamente pelo FastAPI. |
| **Redoc**     | Interface alternativa para documentação da API. |
| **Ruff**      | Ferramenta de formatação e linting de código Python. |

---

## 📄 Documentação

A documentação interativa é gerada automaticamente em tempo de execução:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🐞 Debugging

Você pode adicionar `breakpoint()` no seu código e rodar via terminal para depurar:

```bash
python -m uvicorn aula08.app:app --reload
```

---

## 🧽 Formatação do Código

Para formatar automaticamente todo o código, use:

```bash
poetry run ruff format
```

---

## 🔒 .gitignore

Para ignorar arquivos desnecessários antes de subir no GitHub:

```bash
pipx run ignr -p python > .gitignore
```

Ou adicione manualmente:

```gitignore
__pycache__/
*.pyc
.env
.venv/
```

---

## ✅ Como rodar a aplicação

1. Ative o ambiente:

```bash
poetry shell
```

2. Inicie o servidor local:

```bash
uvicorn aula08.app:app --reload
```

3. Acesse a API:

```
GET http://localhost:8000/novo
```

Retorno esperado:

```json
{
  "message": "Ola Mundo!"
}
```

---

## 📚 Referências

- [Documentação oficial do FastAPI](https://fastapi.tiangolo.com)
- [Pytest](https://docs.pytest.org/)
- [Ruff](https://docs.astral.sh/ruff/)
- [Poetry](https://python-poetry.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Taskipy](https://github.com/illBeRoy/taskipy)

---

## 👨‍💻 Autor

Gustavo – Projeto acadêmico desenvolvido para práticas com FastAPI, testes e ferramentas modernas em Python.
