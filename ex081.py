# Crie um programa que vai ler vários numeros e colocar em uma lista
# Quantos numeros foram digitados
# Mostre a lista ordenada de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista.
numeros = []
while True:
    n = int(input("Digite um número: "))
    numeros.append(n)
    res = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if res == "N":
        break
    
#ordena a lista em forma decrescente:
numeros.sort(reverse=True)

#exibindo a lista já em ordem decrescente, mostrando quantos numeros foram inseridos:
print(numeros)
print(f"Foram digitados {len(numeros)} números...")

#validando se o numero 5 foi encontrado na lista e retornando a informação:
if 5 in numeros:
    pos_num = numeros.index(5) + 1
    print(f"O numero 5 está na lista na posição {pos_num}")
else:
    print("O valor 5 não foi encontrado na lista")
print("fim do programa")
