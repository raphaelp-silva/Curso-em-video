#Jogo de adivinhacao 
from random import randint
n = int(input('Digite um número de 0 até 5: '))
sorteio = randint(0,5)
if n == sorteio:
    print('Parabéns, você é bom mesmo!!! Adivinhou o número!')
else:
    print('eita, errou! tente novamente :) ')

print(f'Voce escolheu {n}, mas a máquina escolheu {sorteio}')
