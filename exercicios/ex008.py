# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

dis = int(input("Digite uma distancia em metros: "))
cen = dis * 100
mil = dis * 1000
km = dis / 1000

print(f"A distancia de {dis} metros, corresponde a :\n"
    f"{cen} Cm\n"
    f"{mil} Ml\n"
    f"{km} Km")