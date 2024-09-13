#Faça um programa que leia 5 valores numericos e guarde-os em uma lista
#Ao final, mostre qual foi o maior e o menor valor digitado e as respectivas posicoes.

lista = [] 

# Lendo os valores numericos:
for n in range (0,5):
    lista.append(int(input("Digite um número: ")))

#exibindo os valores digitados:
print(f"Os valores digitados foram {lista}")

#definindo em variável o maior e o menor valor da lista:
maior = max(lista)
menor = min(lista)

#Exibindo o maior valor e suas posições na lista:
print(f"O maior número foi o {maior} e ele está nas posições ", end ='')
for i, v in enumerate(lista): #utilizando o enumerate para pegar a posicao dos maiores numeros da lista
    if v == max(lista):
        print(f"{i+1}...", end= '')
print()

#Exibindo o menor valor e suas posições na lista:
print(f"O menor número foi o {menor} e ele está nas posições ", end='')
for i, v in enumerate(lista): #utilizando o enumerate para pegar a posicao dos menores numeros da lista
    if v == min(lista):
        print(f"{i+1}...", end= '')
