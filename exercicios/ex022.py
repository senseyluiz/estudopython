# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).

nome = str(input("Digite o nome completo: ")).strip()

print(f"Seu nome com todas as letras maíusculas: {nome.upper()}")
print(f"Seu nome com todas as letras minúsculas: {nome.lower()}")
print(f"Seu nome tem {len(nome)} letras")
