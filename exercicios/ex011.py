# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
are = lar * alt
tin = are / 2

print(f"Uma parede de {lar} mt de largura e {alt} met de altura, tem uma área de {are}m²\n"
    f"Você precisará de {tin:.3f} lts de tinta para pintá-la.")
