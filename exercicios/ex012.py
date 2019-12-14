# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pAtual = float(input("Qual o preço do produto: R$ "))
nPreco = pAtual * 0.95

print(f"O produto que custa R$ {pAtual:.2f}, com 5% de desconto, custará R$ {nPreco:.2f}\n"
    f"O desconto total foi de R$ {pAtual * 0.05:.2f}")
