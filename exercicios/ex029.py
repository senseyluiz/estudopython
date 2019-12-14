# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input("Qual a velocidade do veículo: "))

if vel > 80:
    ult = vel - 80
    multa = ult * 7

    print(f"Ultrapasou {ult} km da velocidade da via.")
    print(f"Você foi multado em R$ {multa:.2f}")
    