# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    res = "podem"
else:
    res = "não podem"

print(f"Essas retas {res} formar um triangulo")