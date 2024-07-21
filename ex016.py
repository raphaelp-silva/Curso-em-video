#Crie um programa que leia um número real e retorne a sua porção inteira
#Criei utilizando a funcao trunc da biblioteca math.

from math import trunc
num = float(input('Digite um numero: '))

print (f'O número é {num} e sua parte inteira é {trunc(num)}')
