from datetime import datetime

def validarData(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome or not data or not local or not categoria:
        print("Todos os campos devem ser preenchidos.")
        return

    if not validarData(data):
        print("Data inválida. Use o formato AAAA-MM-DD.")
        return

    maiorId = 0
    for evento in listaEventos:
        if evento['id'] > maiorId:
            maiorId = evento['id']
    novoId = maiorId + 1

    evento = {
        'id': novoId,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        'participado': False
    }

    listaEventos.append(evento)
    print(f"Evento >{nome}< adicionado com sucesso (ID: {novoId}).")


def listarEvento(listaEventos):
    if not listaEventos:
        print("Nenhum evento foi cadastrado.")
        return 
    
    for evento in listaEventos:
        print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']}")


def procurarEventoPorNome(listaEventos, nome):
    resultados = []
    termo = nome.lower().strip()

    for evento in listaEventos:
        if termo in evento['nome'].lower() or termo in evento['categoria'].lower():
            resultados.append(evento)

    return resultados


def deletarEvento(listaEventos, id):
    encontrou = False
    for evento in listaEventos:
        if evento['id'] == id:
            listaEventos.remove(evento)
            print(f"Evento '{evento['nome']}' removido com sucesso.")
            encontrou = True
            break

    if not encontrou:
        print("Evento não encontrado.")


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
    
    if len(resultados) > 0:
        return resultados
    else:
        print(f"Nenhum evento encontrado na categoria '{categoria}'.")


def marcarEventoAtendido(listaEventos, id):
    encontrou = False
    for evento in listaEventos:
        if evento['id'] == id:
            encontrou = True
            if evento.get('participado'):
                print("Você já marcou este evento como participado.")
            else:
                evento['participado'] = True
                print("Evento marcado como participado.")
            break

    if not encontrou:
        print("Evento não encontrado.")


def gerarRelatorio(listaEventos):
    if not listaEventos:
        print("Não há eventos cadastrados para gerar relatório.")
        return

    total = 0
    participados = 0
    categorias = {}

    for evento in listaEventos:
        total += 1

        if evento.get('participado'):
            participados += 1

        categoria = evento['categoria']
        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

    if total > 0:
        porcentagem = (participados / total) * 100
    else:
        porcentagem = 0

    print("\n" + "=" * 50)
    print("              RELATÓRIO DE EVENTOS")
    print("=" * 50)
    print(f"Total de eventos cadastrados: {total}")
    print(f"Eventos marcados como participados: {participados}")
    print(f"Percentual de participação: {porcentagem:.2f}%")
    print("\nEventos por categoria:")
    
    for categoria, quantidade in categorias.items():
        print(f"- {categoria}: {quantidade} evento(s)")