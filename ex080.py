#Criar um programa onde o usuário insere 5 números cadastrando-o em uma lista
#Essa lista deverá inserir o número na posição correta(sem usar o sort())
#Ao final, mostrar a lista ordenada
numero = []

for c in range(0,5):
    n = int(input("Digite um número: "))
    # verifica se a lista está vazia ou o numero inserido for maior que o ultimo da lista e add no final da lista o valor inserido.
    if len(numero) == 0 or n > numero[-1]:
        numero.append(n)
        print(f"O valor {n} foi inserido na posição {c}")
    else:
        #Percorre a lista e encontra a posição correta para inserir o valor digitao pelo usuário.
        for i in range (len(numero)):
            if n <= numero[i]:
                numero.insert(i,n)
                print(f"O valor {n} foi inserido na posição {i}")
                break
print(numero)
print("FIM DO PROGRAMA")