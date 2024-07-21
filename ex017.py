# Crie um programa que le o cateto oposto e o cateto adjacente de um triangulo retangulo e retorna sua hipotenusa

from math import hypot
cat_oposto = float(input('Qual é o comprimento do cateto oposto? :'))
cat_adjacente = float(input('Qual é o comprimento do cateto adjacente? :'))
hip = hypot(cat_oposto, cat_adjacente)

print (f'Sua hipotenusa é : {hip:.2f}')
