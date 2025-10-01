def displayMenu():
    print("\n" + "=" * 50)
    print("       SISTEMA DE GERENCIAMENTO DE EVENTOS")
    print("=" * 50)
    print("1. Adicionar evento")
    print("2. Listar todos os eventos")
    print("3. Filtrar eventos por categoria")
    print("4. Marcar evento como participado")
    print("5. Gerar relatório")
    print("6. Deletar evento")
    print("0. Sair")


def getEscolhaDoUsuario():
    while True:
        entrada = input("Digite sua opção (0-6): ").strip()
        if entrada.isdigit():
            escolha = int(entrada)
            if 0 <= escolha <= 6:
                return escolha
            else:
                print("Número inválido! Digite um número entre 0 e 6.")
        else:
            print("Entrada inválida! Digite apenas números.")


def filtrarEventosPorCategoria(listaEventos, categoria):
    resultados = []
    busca = categoria.lower().strip()
    
    for evento in listaEventos:
        if evento['categoria'].lower() == busca:
            resultados.append(evento)
    
    if resultados:
        return resultados
    else:
        print(f"Nenhum evento encontrado na categoria '{categoria}'.")


def marcarEventoAtendido(listaEventos, id):
    for evento in listaEventos:
        if evento['id'] == id:
            if evento.get('participado'):
                print("Você já marcou este evento como participado.")
            else:
                evento['participado'] = True
                print("Evento marcado como participado.")
            return  # Sai da função após encontrar o evento

    print("Evento não encontrado.")


def gerarRelatorio(listaEventos):
    if not listaEventos:
        print("Não há eventos cadastrados para gerar relatório.")
        return

    total_eventos = len(listaEventos)
    participados = 0
    categorias = {}

    for evento in listaEventos:
        if evento.get('participado'):
            participados += 1
        
        categoria = evento['categoria']
        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

    porcentagem = (participados / total_eventos) * 100  # total_eventos > 0 garantido acima

    print("\n" + "=" * 50)
    print("              RELATÓRIO DE EVENTOS")
    print("=" * 50)
    print(f"Total de eventos cadastrados: {total_eventos}")
    print(f"Eventos marcados como participados: {participados}")
    print(f"Percentual de participação: {porcentagem:.2f}%")
    print("\nEventos por categoria:")
    
    for categoria, quantidade in categorias.items():
        print(f"- {categoria}: {quantidade} evento(s)")