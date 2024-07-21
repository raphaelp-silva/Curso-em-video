n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O maior número entre os dois é o {n1}')
    print(f'O menor número entre os dois é o {n2}')
elif n1 < n2:
    print(f'O maior número entre os dois é o {n2}')
    print(f'O menor número entre os dois é o {n1}')
else:
    print ('Os números são iguais')
