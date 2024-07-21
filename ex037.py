num = int(input('Digite um numero inteiro: '))
print ('''Escolha uma das bases para conversão
       [1] converter para BINÁRIO
       [2] converter para OCTADECIMAL
       [3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O numero {num} em BINARIO é {bin(num)}')
elif opcao == 2:
    print(f'O numero {num} em OCTADECIMAL é {oct(num)}')
elif opcao == 3:
    print(f'O numero {num} em HEXADECIMAL é {hex(num)}')
else:
    print('Opção inválida, tente novamente. ')
