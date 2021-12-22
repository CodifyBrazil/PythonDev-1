"""
Sera um sistema completo de integracao com enderecos aos marketplaces, lojas, tudo que envolva enderecos.

Aquela complicacao de ficar indo em marketplace, em marketplace para mudar seu endereco, por que voce mudou de casa, cidade, ou país.

Em um unico sistema, voce vai cadastrar seu endereco, e pronto o restante nós fazemos, cadastramos seu endereco em todos os marketplaces que voce desejar.

Voce precisara logar nos marketplace em nossa plataforma uma unica vez, e aceitar os termos de uso, após iso, nas proximas vezes, apenas entrar em nosso sistema e mudar seu endereco atual, pronto, facil, mais facil que pegar doce de crianca rsrs.

"""
# get -> pega dados
# post -> envia dados
# path -> atualiza dados
# delete -> deleta dados

import requests

busca_cep = 'https://cep.awesomeapi.com.br/json/'
database = 'https://teste-python-8f062-default-rtdb.firebaseio.com/.json'

# marketplaces
marketplaces = {
        1: 'Mercado Livre',
        2: 'Shopee',
        3: 'B2W',
        4: 'Casas Bahia',
}


# Pegar dados do cliente (cep, Nome)
def db(arg='get', data=1):
    if arg == 'get':
        response = requests.get(database)
        print(response.json())

    if arg == 'post':
        data = {}
        response.post(database, data)
        print(response.json())

    if arg == 'path':
        reponse.path(database, data)
        print(response.json())

    if arg == 'delete':
        response = requests.delete(database, data)
        print(response.json())




# Mostrar marketplaces disponiveis pedir para ele
for mk, mv in marketplaces.items():
    print(mv)


# selecionar quais ele quer adicionar
# Adicionar os enderecos nos marketplaces
# Mostrar que deu certo
