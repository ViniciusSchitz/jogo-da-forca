import os
import random
from palavras_secretas.array_palavras import palavras

index_aleatorio = random.randint(0, 10)
palavra_secreta = palavras[index_aleatorio]
letras_acertadas = ''
numero_tentativas = 0
numero_tentativas_maxima = 6

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    if letra_digitada not in palavra_secreta:
        numero_tentativas_maxima -= 1

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)
    print('Tentativas restantes:', numero_tentativas_maxima)

    if numero_tentativas_maxima == 0:
        os.system('cls')
        print('VOCÊ PERDEU !!!')
        print('A palavra era: ' + palavra_secreta)
        break


    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        numero_tentativas_maxima = 7
        break