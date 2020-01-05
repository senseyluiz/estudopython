#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = ano - nasc
if idade < 18:
    print(f"Ainda não é hora de se alistar. Faltam {18 - idade} anos")
elif idade == 18:
    print("Você precisa se alistar imediatamente. BOA SORTE!!!")
elif idade > 18:
    print(f"Seu alistamento foi em {nasc + 18} há {ano - (nasc + 18)} anos atrás.")
