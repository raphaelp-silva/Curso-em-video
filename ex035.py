print('-=' *20 )
print('Validador de triangulos do Raphael')
print('-=' *20 )
r1 = float(input('Digite o tamanho do primeiro segmento: '))
r2 = float(input('Digite o tamanho do segundo segmento: '))
r3 = float(input('Digite o tamanho do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #regra matematica para validar o triangulo, um lado tem que ser menor que a soma dos outros 2 lados do triangulo.
    print('Poderá ser formado um triangulo')
else:
    print('Não poderá ser formado um trinagulo')