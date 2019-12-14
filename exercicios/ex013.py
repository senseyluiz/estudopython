# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sAtual = float(input("Qual o salário do funcionário: R$ "))
nSalario = sAtual * 1.15
aumento = sAtual * 0.15

print(f"Com o salário de R$ {sAtual:.2f}, terá um aumento de R$ {aumento:.2f} referente a 15%\n"
    f"O novo salário será de R$ {nSalario:.2f}")
    