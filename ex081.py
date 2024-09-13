# Crie um programa que vai ler vários numeros e colocar em uma lista
# Quantos numeros foram digitados
# Mostre a lista ordenada de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista.
numeros = []
num_digitados = 0
while True:
    n = int(input("Digite um número: "))
    numeros.append(n)
    num_digitados += 1
    res = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if res == "N":
        break
numeros.sort(reverse=True)
print(numeros)
print(f"Foram digitados {num_digitados} números...")
for i in numeros:
    if i == 5:
        pos_num = numeros.index(5) + 1
        print(f"O numero 5 está na lista na posição {pos_num}")
    else:
        print("O valor 5 não foi encontrado na lista")
        break
print("fim do programa")
