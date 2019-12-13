# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input("Digite um número: "))
dob = num * 2
tri = num * 3
rai = num ** (1/2)

print(f"O dobro de {num} é {dob}\n"
    f"O triplo de {num} é {tri}\n"
    f"A raiz quadrada de {num} é {rai}")
