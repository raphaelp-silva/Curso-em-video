# Criar um programa que gera aleatoriamente 5 numeros e os coloquem em uma tupla
# Mostrar a lista gerada, e o menor e o maior valor que estão na tupla.
from random import randint

maior = menor = i = num = quant = 0
num = tuple(randint(1, 10) for i in range(0, 5))

# COMO EU FIZ SOZINHO (sem saber do max e min):

# for elemento in num:
#     quant += 1
#     if quant == 1:
#         menor = maior = elemento
#     else:
#         if elemento > maior:
#             maior = elemento
#         if elemento < menor:
#             menor = elemento

print(f"A tupla é: {num}")
print(f"O MAIOR numero foi: {max(num)}") # max e min é uma facilidade o Python que funciona com tuplas
print(f"O MENOR numero foi: {min(num)}")
