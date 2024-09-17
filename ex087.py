#Aprimorando o exercicio 86
#Somando todos os valores pares digitados
#Somando os valores da terceira coluna
#Exibindo o maior valor da segunda linha

#declarando uma matriz de 3x3 inicialmente preenchida com 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
valores_pares = soma_coluna = 0 

#criando 2 laços de repetição para ler os valores e preencher a matriz 
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f"Digite um numero para a posição {[l]}{[c]}: "))
        if matriz[l][c] % 2 == 0:
            valores_pares += matriz[l][c]

#somando os valores da terceira coluna
for l in range (0,3):
    soma_coluna += matriz[l][2]

#mostrando a matriz formatada onde cada célula ocupa 5 caracteres de largura
print("=-"*20)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()

print(f"A soma dos valores pares digitados foi: {valores_pares}")
print(f"A soma dos valores da terceira coluna foi: {soma_coluna}")

#exibindo o maior valor da segunda linha
print(f"O maior valor da segunda linha é o : {max(matriz[1])}")
