#Crie um programa onde o usuário possa digitar numeros e cadastra-los em uma lista
#O programa não deve aceitar números repetidos
#No final, serão exibidos todos os valores digitados na lista em ordem crescente
lista = []
while True:
    #validando se o valor inserido é valido:
    try:
        n = int(input("Digite um número: "))
    except ValueError:
        print("Por favor, insira um número válido!")
        continue
    #validando se o valor inserido é duplicado na lista:
    if n in lista:
        print("Esse valor já foi digitado!")
    else:
    #adicionando o valor inserido à lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
    #perguntando ao usuário se deseja continuar no looping e inserir outro valor:
    res = str(input("Voce deseja continuar? [S/N]")).upper().strip()[0]
    if res == "N":
        break
print("=-" *20)
#modifica a lista original e a coloca em ordem crescente:
lista.sort()
print(f"A lista criada foi {lista}")
print("=-" *20)
print("fim do programa!")
