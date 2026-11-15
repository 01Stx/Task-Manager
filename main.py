from database import (
    criar_tabela,
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa,
)

def mostrar_tarefas():
    tarefas = listar_tarefas()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n--- LISTA DE TAREFAS ---")

    for tarefa_id, titulo, descricao, concluida in tarefas:
        status = "Concluída" if concluida else "Pendente"

        print(f"\nID: {tarefa_id}")
        print(f"Título: {titulo}")
        print(f"Descrição: {descricao or 'Sem descrição'}")
        print(f"Status: {status}")


def ler_id():
    try:
        return int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("Erro: digite um número inteiro válido.")
        return None


def main():
    criar_tabela()

    while True:
        print("\n" + "=" * 35)
        print("         TASK MANAGER")
        print("=" * 35)
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição (opcional): ")

            try:
                tarefa_id = adicionar_tarefa(titulo, descricao)
                print(f"\nTarefa cadastrada! ID: {tarefa_id}")
            except ValueError as erro:
                print(f"\nErro: {erro}")

        elif opcao == "2":
            mostrar_tarefas()

        elif opcao == "3":
            mostrar_tarefas()
            tarefa_id = ler_id()

            if tarefa_id is not None:
                if concluir_tarefa(tarefa_id):
                    print("\nTarefa marcada como concluída!")
                else:
                    print("\nTarefa não encontrada.")

        elif opcao == "4":
            mostrar_tarefas()
            tarefa_id = ler_id()

            if tarefa_id is not None:
                if excluir_tarefa(tarefa_id):
                    print("\nTarefa excluída!")
                else:
                    print("\nTarefa não encontrada.")

        elif opcao == "5":
            print("\nEncerrando o Task Manager. Até mais!")
            break

        else:
            print("\nOpção inválida. Escolha de 1 a 5.")


if __name__ == "__main__":
    main()