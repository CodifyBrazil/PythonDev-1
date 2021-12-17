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

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] {rv}')
    r = input('Qual a Resposta certa ? ')
    r = r.upper()
    if r == pv['resposta_certa']:
        print('UHUUUL, voce acertou!')
        pontos += 1
    else:
        print('AAAAH, que pena, voce errou!')

print(f'voce fez {pontos} pontos.')
