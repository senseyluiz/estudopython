# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input("Qual o cateto oposto: "))
ca = float(input("Qual o cateto adjacente: "))
hi = hypot(ca, co)

print(f"O cumprimento da Hipotenusa é: {hi:.2f}")