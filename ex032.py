from datetime import date

ano = int(input('Qual ano você quer analisar? Coloque 0 para o ano atual:'))

if ano == 0:
    ano = date.today().year #serve para pegar o ano atual da máquina que está rodando o programa
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O ano de {ano} é um ano BISSEXTO!')
else:
    print(f'O ano de {ano} não é um ano BISSEXTO!')