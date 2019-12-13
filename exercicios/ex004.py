# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input("Digite algo: ")

print(f"O tipo primitivo de {palavra} é {type(palavra)}")
print(f"Só tem espaços? {palavra.isspace()}")
print(f"É alfabético? {palavra.isalpha()}")
print(f"É um número? {palavra.isnumeric()}")
print(f"É alfanumérico? {palavra.isalnum()}")
print(f"Está em maíusculas? {palavra.isupper()}")
print(f"está em minúsculo: {palavra.islower()}")
print(f"Está capitalizada? {palavra.istitle()}")
