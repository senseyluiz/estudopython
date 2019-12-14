# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

pc = random.randint(0,5)

print("=-" * 25)
print("Tente adivinhar o número que o computador escolheu")
print("=-" * 25)

jog = int(input("Digite um número entre 0 e 5: "))

if jog == pc:
    print("Parabéns, você acertou. ")
else:
    print("Você errou.")
