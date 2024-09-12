n1 = float(input('Digite a nota da p1: '))
n2 = float(input('Digite a nota da p2: '))
m = (n1+n2) / 2
print (f'Sua média foi {m:.1f}')
if m >= 6.0: 
    print('Sua média foi boa, PARABÉNS!!!')
else: 
    print('Sua média foi ruim, ESTUDE MAIS!!!')
