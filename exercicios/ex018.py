#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = int(input("Digite o ângulo desejado: "))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f"Com o ângulo de {ang}° temos:\n"
    f"Seno : {sen:.2f}\n"
    f"Cosseno : {cos:.2f}\n"
    f"Tangente: {tan:.2f}")
