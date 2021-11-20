dica = 'animal'
print(f"""
  
  ------------------------------
  ------- JOGO DA FORCA --------
  ------------ 1.0 -------------
  dica: {dica}
""")

palavra_secreta = 'gato'
digitadas = []
chances = 10
tentativas = 0

while True:

  if chances <= 0:
    print(f'Voce perdeu, voce tem {chances} chances')
    break

  letra = input('Digite uma letra: ')

  if len(letra) > 1:
    print('Digite apenas uma letra por vez. ')
    continue

  digitadas.append(letra)
  
  if letra in palavra_secreta:
    print(f'UHUUUL voce acertou a letra "{letra}"\n')

  else:
    print(f'AAAH que pena errou a letra "{letra}"\n')
    digitadas.pop()
    chances -= 1
    
  mostra_palavra = ''
  for palavra in palavra_secreta:
    if palavra in digitadas:
      mostra_palavra += palavra
    else:
      mostra_palavra += '*'

  if mostra_palavra == palavra_secreta:
    print(f'Parabens a palavra secreta é "{palavra_secreta}"').upper
    break
  
  tentativas += 1

  print(f'{mostra_palavra}')
  print(f'voce tem {chances} chances \n')
      
