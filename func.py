from datetime import datetime

def validarData(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome or not data or not local or not categoria:
        print('Todos os campos devem ser preenchidos.')
        return
    if not validarData(data):
        print('Data inválida. Use o formato AAAA-MM-DD.')
        return
    novoId = len(listaEventos) + 1
    evento = {
        'id': novoId,
        'nome': nome,
        'data': data,
        'local': local,
        'categoria': categoria
    }
    listaEventos.append(evento)
    print(f'Evento >{nome}< adicionado com sucesso (ID: {novoId}).')

def listarEvento(listaEventos):
    if not listaEventos:
        print('Nenhum evento foi cadastrado.')
        return 
    for evento in listaEventos:
        print(f'ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']}')

def procurarEventoPorNome(listaEventos, nome):
    resultados = []
    termo = nome.lower().strip()
    for evento in listaEventos:
        if termo in evento['nome'].lower() or termo in evento['categoria'].lower():
            resultados.append(evento)
    return resultados

def deletarEvento(listaEventos, id):
    for evento in listaEventos:
        if evento['id'] == id:
            listaEventos.remove(evento)
            print(f'Evento >{evento['nome']}< removido com sucesso.')
            break
    else:
        print('Evento não encontrado.')