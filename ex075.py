# Criar um programa que leia 4 numeros e armazene-os em tupla
# Apresentar quantas vezes apareceu o numero 9
# Apresentar em que posicao ficou o primeiro numero 3
# Apresentar quais foram os numeros pares
num_nove = 0
lista = []  # criando uma lista vazia
pares = []
for i in range(4):  # percorrendo a lista
    num = int(input(f"Digite o numero {i+1}: "))
    lista.append(num)  # adicionando o numero digitado à lista
    if num % 2 == 0:
        pares.append(num)

tupla_de_numeros = tuple(lista)  # convertendo a lista em tupla
tupla_de_pares = tuple(pares)
print(tupla_de_numeros)
if 3 in tupla_de_numeros:
    print(f"O primeiro numero 3 ficou na posição {tupla_de_numeros.index(3)+1}")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print(f"O Número 9 apareceu {tupla_de_numeros.count(9)} vezes")
print(f"Os números pares são {tupla_de_pares}")
