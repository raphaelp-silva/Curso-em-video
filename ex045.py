from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)

print("""
Suas opções
[0]PEDRA
[1]PAPEL
[2]TESOURA""")

sua_jogada = int(input("Qual é a sua jogada?"))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POOO!")

print("-=" *11)
print(f"Você jogou {itens[sua_jogada]}")
print(f"O computador jogou {itens[computador]}")
print("-=" *11)

if computador == 0: #Se o computador jogou PEDRA
    if sua_jogada == 0: 
        print("\033[33mEmpatou!")
    elif sua_jogada == 1: 
        print("Você \033[32mVENCEU\033[m o computador!")
    elif sua_jogada == 2: 
        print("Você \033[31mPERDEU\033[m para o computador!")
    else:
        print("Jogada inválida!")
elif computador == 1: #Se o computador jogou PAPEL
    if sua_jogada == 0: 
        print("Você \033[31mPERDEU\033[m para o computador!")
    elif sua_jogada == 1: 
        print("\033[33mEmpatou!")
    elif sua_jogada == 2: 
        print("Você \033[32mVENCEU\033[m o computador!")
    else:
        print("Jogada inválida!")
elif computador == 2: #Se o computador jogou TESOURA
    if sua_jogada == 0: 
        print("Você \033[32mVENCEU\033[m o computador!")
    elif sua_jogada == 1: 
        print("Você \033[31mPERDEU\033[m para o computador!")
    elif sua_jogada == 2:
        print("\033[33mEmpatou!")
    else:
        print("Jogada inválida!")
