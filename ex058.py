from random import randint
computador = randint(0,10)
print("Sou eu, seu computador! Pensei em um número de 0 a 10... você consegue acertar?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Digite seu palpite: "))
    palpites +=1
    if jogador == computador:
        acertou = True
    else: 
        if jogador > computador:
            print("Menos...tente novamente!")
        elif jogador < computador:
            print("Mais... tente novamente!")
print(f"Acertou! você precisou de {palpites} tentativas.")
