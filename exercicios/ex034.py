# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Qual o salário do funcionário? R$ "))

if sal > 1250:
    novosal = sal * 1.1
else:
    novosal = sal * 1.15

print(f"Com salário de R$ {sal:.2f} terá um aumento de R$ {novosal - sal:.2f} e passa a receber R$ {novosal:.2f}")