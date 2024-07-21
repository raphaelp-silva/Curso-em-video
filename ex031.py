dist = int(input('Qual é a distancia da sua viagem? :'))

if dist >= 200:
   preco1 = dist * 0.45
   print(f'Você pagará R${preco1} reais por essa viagem.') 
else:
   preco2 = dist * 0.50
   print(f'Voce pagará R${preco2} reais por essa viagem.')
print('BOA VIAGEM! VOLTE SEMPRE...')
