# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão: \n"
      "[1] Converter para BINÁRIO\n"
      "[2] Converter para OCTAL\n"
      "[3] Converter para HEXADECIMAL")

opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f"O número {num} convertido para BINÁRIO é: {bin(num)[2:]}")
elif opcao == 2:
    print(f"O número {num} convertido para OCTAL é: {oct(num) [2:]}")
elif opcao == 3:
    print(f"O número {num} convertido para HEXADECIMAL é: {hex(num) [2:]}")
else:
    print("Opção incorreta.")
