 # 1. Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área.
import math


raio = int(input("Digite o raio do círculo: "))
print("Raio da circunferência: {}".format(pow(raio,2) * math.pi))