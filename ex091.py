#Criar um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
from random import randint
from time import sleep  
from operator import itemgetter

dados = {}

#Simulando o lançamento de dados de cada jogador
for i in range (1,5):
    dados[f'Jogador {i}'] = randint(1,6)

#exibindo os resultados
print("Jogos soretados")
for k, v in dados.items():
    print(f"O {k} tirou {v}")
    sleep(.8)

#Criando a lista do ranking e ordenando por ordem decrescente
ranking = ()
ranking = sorted(dados.items(), key=itemgetter(1), reverse= True)

#Exibindo o resultado final em ranking
print("\n-=-=-=-= RAKING FINAL =-=-=-=-")
for i, v in enumerate(ranking):
    print(f"{i+1}° Lugar -> {v[0]} com {v[1]}")
    sleep(.8)

print("\nFIM DO JOGO! ! ! ")