# Task Manager

Aplicação de gerenciamento de tarefas desenvolvida em Python, utilizando SQLite para armazenamento persistente de dados.

## Funcionalidades

- Adicionar tarefas com título e descrição.
- Listar tarefas cadastradas.
- Marcar tarefas como concluídas.
- Excluir tarefas.
- Armazenar informações em banco de dados SQLite.
- Testes automatizados com unittest.

## Tecnologias utilizadas

- Python 3
- SQLite
- unittest

## Como executar

1. Clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

## Como executar os testes

```bash
python -m unittest discover -s . -p "test_*.py" -v
```

## Estrutura do projeto

```text
Task_Manager/
├── main.py
├── database.py
├── test_database.py
├── README.md
├── .gitignore
└── tarefas.db (gerado automaticamente)
```

## Objetivo

Projeto desenvolvido para praticar programação em Python, operações CRUD, integração com banco de dados SQLite e testes automatizados.

## Autor

Desenvolvido como projeto de estudo e portfólio.