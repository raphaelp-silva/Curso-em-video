frase = str(input('Digite uma frase: ')).upper().strip()
print (f'A frase possui {frase.count('A')} vezes a letra A')
print (f'A primeira letra A aparece na posição {frase.find('A')+1}') #usando find para procurar a letra na primeira posicao (o +1 serve para adequar a posicao que os humanos imaginam)
print (f'A ultima posição da letra A é {frase.rfind('A')+1}') #usando rfind para comecar a procurar da direita
