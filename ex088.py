#Criar um programa que criará palpites da mega sena
#O programa vai perguntar quanto jogos serão gerados
#Sortear um conjunto de 6 numeros de 1 a 60 para cada jogo solicitado
#Cadastrar todos os jogos em uma lista composta.
from random import randint
from time import sleep
print("------ JOGO DA MEGA SENA ------")
palpites = int(input("Quantos jogos você quer fazer?"))
lista_jogos = []
for i in range (0,palpites):
    lista_temporaria = []
    while len(lista_temporaria) < 6: #garante que cada jogo terá 6 números
        n_sorteado = randint(1,60)
        if n_sorteado not in lista_temporaria: #verificando se o número sorteado já está na lista, caso não, ele é adicionado à lista.
            lista_temporaria.append(n_sorteado)
    lista_jogos.append(sorted(lista_temporaria[:]))
    lista_temporaria.clear()
 
#Exibindos os resultados de forma ordenada e crescente
for index, jogo in enumerate(lista_jogos,1):
    print(f"Jogo {index}: {jogo}")
    sleep(0.4)
print("-------------------------------")
print(" Boa sorte, agora vai!!! ")
