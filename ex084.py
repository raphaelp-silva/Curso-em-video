#Criar um programa que leia nome e peso de varias pessoas e o amarzene em lista
#Mostre quantas pessoas foram cadastradas, uma listagem com as mais pesadas e outra com as mais leves
cadastro = list()
dados = list()
maior = menor = 0
while True:
    nome = str(input("Digite o Nome: "))
    peso = float(input("Digite o peso: "))
    #Adicionando nome e peso recebidos na lista de dados (temporária)
    dados.append(nome)
    dados.append(peso)
    
    if len(cadastro) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    #Adicionando cópia da lista 'dados'
    cadastro.append(dados[:])
    #Limpando os dados para a próxima pessoa
    dados.clear()

    resp = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if resp == 'N':
        break

print(f"Foram cadastradas {len(cadastro)} pessoas")
print(f"O maior peso foi {maior} Kg. Peso de ", end ='')
for pessoa in cadastro:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}] ", end = '')
print()
print(f"O menor peso foi {menor} Kg. Peso de ", end ='')
for pessoa in cadastro:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}] ", end ='')
