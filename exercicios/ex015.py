#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input("Quantos Km foram rodados? "))
dias = int(input("Quantos dias foram alugados: "))
pdias = 60 * dias
pkm = km * 0.15
total = pdias + pkm

print(f"Aluguel do carro")
print('=' * 30)
print(f"{dias} Dias alugados: R$ {pdias:.2f}")
print(f"{km}Km Rodados: R$ {pkm:.2f}")
print(f"Total a pagar: {total:.2f}")
print("=" * 30)
