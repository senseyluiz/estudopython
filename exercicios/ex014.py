# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Qual a temperatura em °C: "))
f = 1.8 * c + 32

print(f"{c:.1f}°C convertidos para °F é: {f:.1f}°F")
