#Criar um programa que leia varios números e o armazene em uma lista
#Criar 2 listas extras que vão dividir os valores entre par e impar
#Mostrar o conteúdo das 3 listas
num_geral = []
num_par = []
num_impar = []

while True:
#lendo o valor de entrada e adicionando-o a lista de numeros gerais
    num_geral.append(int(input("Digite um número: ")))
    resp = str(input("Deseja digitar mais um numero? [S/N]")).upper().strip()[0]
    if resp == 'N':
#validando se o valor é par para adicioná-lo a lista de pares ou se não for par, na lista de ímpares:
        for i in num_geral:
            if i % 2 == 0:
                num_par.append(i)
            else:
                num_impar.append(i)
        break

#Exibindo os resultados pedidos no enunciado:
print(f"Os valores digitados foram {num_geral}")
print(f"Os valores pares são {num_par}")
print(f"Os valores ímpares são {num_impar}")