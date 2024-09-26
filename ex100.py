# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
# A primeira função vai sortear 5 números e colocá-los dentro da lista
# a segunda função vai mostrar a soma entre todos os números pares sorteados pela função anterior
from random import randint
from time import sleep
numeros = []


def sorteia():
    print("Sorteando 5 valores para a lista...")
    for n in range(0, 5):
        sorteio = randint(0, 50)
        numeros.append(sorteio)
        print(f"{sorteio} ", end="", flush=True)
        sleep(0.3)
    print("\nPRONTO! SORTEADO!")

def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f"A soma dos números pares é: {soma}")


sorteia()
somaPar()
