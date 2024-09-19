#Criar um programa que leia nome e duas notas de varias alunos guardando-os em uma lista composta
#Ao final, mostrar um boletim contendo a média de cada um e permitindo que o usuário consulte as notas (individualmente) caso queira

alunos = []
lista_temp = []
while True:
    nome = str(input("Digite o nome do aluno: "))
    nota_1 = float(input("Digite a nota da P1: "))
    nota_2 = float(input("Digite a nota da P2: "))
    media = (nota_1 + nota_2) / 2

    #Adicionando os dados na lista 
    lista_temp.append(nome)
    lista_temp.append(nota_1)
    lista_temp.append(nota_2)
    lista_temp.append(media)
    
    #Salvando os dados e limpando a lista temporária
    alunos.append(lista_temp[:])
    lista_temp.clear()
    
    resp = str(input("Deseja cadastrar outro aluno? [S/N]")).upper().strip()[0]
    if resp == 'N':
        break

print("----- MÉDIA DOS ALUNOS -----")
print(f'{"No.":<4}{"Aluno":<10}{"Média":>8}') #Exibindo e formatando o cabeçalho da exibição

#percorrendo a lista e exibindo o nome de cada aluno e sua respectiva média
for i, aluno in enumerate(alunos):
    print(f"{i:<4} {aluno[0]:<10} {aluno[3]:>8.1f}")

#Consultando as notas individuais
while True: 
    opc = int(input("Digite o número do Aluno para visualizar as notas (999 para parar)"))
    if opc == 999:
        break
    if opc <= len(alunos) - 1:
        print(f"Notas de {alunos[opc][0]} são {alunos[opc][1]} e {alunos[opc][2]}")

print("Fim do programa")