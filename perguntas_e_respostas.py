perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quantos é 2+2?',
        'respostas': {
            'A': 2,
            'B': 5,
            'C': 4
        },
        'resposta_certa': 'C'
    },
    'Pergunta 2': {
        'pergunta': 'Quantos é 6+2?',
        'respostas': {
            'A': 8,
            'B': 9,
            'C': 5
        },
        'resposta_certa': 'A'
    },
    'Pergunta 3': {
        'pergunta': 'Quantos é 3+8?',
        'respostas': {
            'A': 12,
            'B': 11,
            'C': 5
        },
        'resposta_certa': 'B'
    },
    'Pergunta 4': {
        'pergunta': 'Quantos é 1+2?',
        'respostas': {
            'A': 3,
            'B': 2,
            'C': 1
        },
        'resposta_certa': 'A'
    },
}

pontos = 0

#interaveis do dicionario
for pk, pv in perguntas.items():
  #printa a pergunta
    print(f'{pk}: {pv["pergunta"]}')

    # faz a interacao das alternativas
    for rk, rv in pv['respostas'].items():
      #printa as alternativas
        print(f'[{rk}] {rv}')
      
    r =''

    #se o usuario digitar mais de uma letra, fiuca no loop
    while r == '' or r == ' ':
      #pergunta a resposta correta
      r = input('Qual a Resposta certa ? ')
      #deixa a resposta em letra maiuscula
      r = r.upper()

      if len(r) > 1:
        print('Só pode digitar 1 letra na resposta.')
        r = ''
        continue

    #confere se a resposta enviada é a correta
    if r == pv['resposta_certa']:
        print('UHUUUL, voce acertou!')
        # se for correta, adiciona 1 ponto a cada questao certa
        pontos += 1
    else:
        print('AAAAH, que pena, voce errou!')

#conta para ver quantos % acertou de questoes
porcentagem = pontos/len(perguntas) * 100
#printa quantos pontos fez, e a porcentagem de acertos
print(f'voce fez {pontos} pontos, e acertou {porcentagem:.2f}% das questoes.')
