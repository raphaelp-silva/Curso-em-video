#Criar um programa que leia 7 valores inseridos pelo usuário e cadastrá-lo em uma unica lista.
#Separando-os em pares e impares
#Ao final, mostrar os valores separados em ordem crescente

#Lista principal com suas sublistas, para para pares e outra para impares.
lista_princ = [[],[]]
#Laço de repetição para coletar 7 valores inserido pelo usuário
for i in range (1,8):
    num = int(input(f"Digite {i}º número: "))
    if num % 2 ==0: # se for um número PAR
        lista_princ[0].append(num)
    else: # se não é par, logo é um número IMPAR
        lista_princ[1].append(num)

print('-=' * 20)
print(f"Os números pares são {sorted(lista_princ[0])}") #Exibe a lista de pares em ordem crescente
print(f"Os números ímpares são {sorted(lista_princ[1])}") #Exibe a lista de impares em ordem crescente
