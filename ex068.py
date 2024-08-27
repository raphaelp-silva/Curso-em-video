# Game de jogar par ou impar contra o computador
# O programa encerra quando o jogador perde e a soma das vitórias é exibida ao final
from random import randint 
from time import sleep

max_win = 0
print("=-" *10, "Jogo de par ou impar ","=-"*10)
while True:
    computador = randint(1,10)
    n = int(input("Digite o valor: "))
    res = n + computador 
    cond = str(input("Você quer par ou impar? [P/I] ")).strip().upper()
    print("1, 2, 3, e já!")
    sleep(1)
    print(f"O computador escolheu {computador}")
    sleep(1)
    if res % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"
    if resultado == cond:
        print(f"O jogo deu {res}")
        sleep(1)
        print("Você venceu!")
        max_win += 1
    else:
        print(f"O jogo deu {res}")
        sleep(1)
        print("Você perdeu!")
        break
print("FIM DE JOGO ! ! ! ")
print(f"Você venceu {max_win} vezes seguidas!")