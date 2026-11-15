from contextlib import contextmanager
import sqlite3

DB_NAME = "tarefas.db"


@contextmanager
def conectar():
    conexao = sqlite3.connect(DB_NAME)
    try:
        yield conexao
        conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        conexao.close()

def criar_tabela():
    """Cria a tabela de tarefas caso ainda não exista."""
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT DEFAULT '',
                concluida INTEGER NOT NULL DEFAULT 0
            )
        """)

def adicionar_tarefa(titulo, descricao=""):
    """Adiciona uma nova tarefa"""
    titulo = titulo.strip()

    if not titulo:
        raise ValueError("O título da tarefa não pode ser vazio.")

    with conectar() as conexao:
        cursor = conexao.execute(
            "INSERT INTO tarefas (titulo, descricao) VALUES (?, ?) ",
            (titulo, descricao.strip())
        )
        return cursor.lastrowid


def listar_tarefas():
    """Retorna todas as tarefas cadastradas."""
    with conectar() as conexao:
        cursor = conexao.execute(
            """
            SELECT id, titulo, descricao, concluida
            FROM tarefas
            ORDER BY id
            """
        )
        return cursor.fetchall()

def concluir_tarefa(tarefa_id):
    """Marca uma tarefa como concluída."""
    with conectar() as conexao:
        cursor = conexao.execute(
            "UPDATE tarefas SET concluida = 1 WHERE id = ?",
            (tarefa_id,)
        )
        return cursor.rowcount > 0


def excluir_tarefa(tarefa_id):
    """Exclui uma tarefa pelo ID."""
    with conectar() as conexao:
        cursor = conexao.execute(
            "DELETE FROM tarefas WHERE id = ?",
            (tarefa_id,)
        )
        return cursor.rowcount > 0


if __name__ == "__main__":
    criar_tabela()
    print("banco de dados inicializado com sucesso!")