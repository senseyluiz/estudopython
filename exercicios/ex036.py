# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valcasa = float(input("Qual o valor da casa: R$ "))
sal = float(input("Salário do comprador: R$ "))
anos = int(input("Em quantos anos vai pagar: "))
valmax = sal * 0.30
prest = anos * 12
valprest = valcasa / prest

print(f"Para pagar uma casa no valor de R$ {valcasa:.2f} em {anos} anos, a prestação será de: R${valprest:.2f} ")

if valprest <= valmax :
    print("Empréstimo Aprovado com Sucesso!")
else:
    print("Empréstimo Negado!")


