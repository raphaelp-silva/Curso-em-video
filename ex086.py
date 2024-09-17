#Crie um programa que declare uma matriz de dimensao 3x3 e preencha com valores lidos pelo tecldo
#No final, mostre a matriz na tela, com a formatação correta.

#declarando uma matriz de 3x3 inicialmente preenchida com 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
#criando 2 laços de repetição para ler os valores e preencher a matriz 
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f"Digite um numero para a posição {[l]}{[c]}: "))

print("=-"*20)
#mostrando a matriz formatada onde cada célula ocupa 5 caracteres de largura
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
