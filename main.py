from func import (
    adicionarEvento,
    listarEvento,
    filtrarEventosPorCategoria,
    marcarEventoAtendido,
    gerarRelatorio,
    deletarEvento
)

def exibirMenu():
    print("\n=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Deletar Evento")
    print("0. Sair")

def main():
    listaEventos = []

    while True:
        exibirMenu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do evento: ").strip()
            data = input("Data (AAAA-MM-DD): ").strip()
            local = input("Local: ").strip()
            categoria = input("Categoria: ").strip()
            adicionarEvento(listaEventos, nome, data, local, categoria)

        elif opcao == "2":
            listarEvento(listaEventos)

        elif opcao == "3":
            categoria = input("Digite a categoria: ").strip()
            eventos_filtrados = filtrarEventosPorCategoria(listaEventos, categoria)
            if eventos_filtrados:
                for evento in eventos_filtrados:
                    print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']}")
        
        elif opcao == "4":
            try:
                id_evento = int(input("Digite o ID do evento: ").strip())
                marcarEventoAtendido(listaEventos, id_evento)
            except ValueError:
                print("ID inválido. Digite um número.")

        elif opcao == "5":
            gerarRelatorio(listaEventos)

        elif opcao == "6":
            try:
                id_evento = int(input("Digite o ID do evento que deseja deletar: ").strip())
                deletarEvento(listaEventos, id_evento)
            except ValueError:
                print("ID inválido. Digite um número.")

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
