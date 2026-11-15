import os
import tempfile
from typing import Self
import unittest
from unittest.mock import patch

import database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.arquivo_temporario = tempfile.NamedTemporaryFile(
            suffix=".db", delete=False
        )
        self.arquivo_temporario.close()

        self.patch_db = patch.object(
            database, "DB_NAME", self.arquivo_temporario.name
        )
        self.patch_db.start()
        database.criar_tabela()


    
    def tearDown(self):
        self.patch_db.stop()

        if os.path.exists(self.arquivo_temporario.name):
            os.remove(self.arquivo_temporario.name)



    def test_adicionar_tarefa(self):
        tarefa_id = database.adicionar_tarefa(
            "Estudar Python", "Praticar SQLite"
        )
        self.assertGreater(tarefa_id, 0)

    def test_listar_tarefas(self):
        database.adicionar_tarefa("Estudar Python")
        tarefas = database.listar_tarefas()

        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0][1], "Estudar Python")

    def test_concluir_tarefa(self):
        tarefa_id = database.adicionar_tarefa("Tarefa de teste")

        resultado = database.concluir_tarefa(tarefa_id)
        tarefas = database.listar_tarefas()

        self.assertTrue(resultado)
        self.assertEqual(tarefas[0][3], 1)

    def test_excluir_tarefa(self):
        tarefa_id = database.adicionar_tarefa("Tarefa temporária")

        resultado = database.excluir_tarefa(tarefa_id)

        self.assertTrue(resultado)
        self.assertEqual(database.listar_tarefas(), [])

    def test_titulo_vazio(self):
        with self.assertRaises(ValueError):
            database.adicionar_tarefa("   ")


if __name__ == "__main__":
    unittest.main()