# simulador de financiamento de casa

valor_imovel = float(input('Qual é o valor do imóvel a ser financiado? R$ '))
salario = float(input('Qual é o valor do seu salário? R$ '))
prazo = int(input('Em quantos anos será feito o pagamento? '))

fin = valor_imovel/ (prazo *12)

if fin <= salario*0.30:
    print (f'Seu financiamento foi \033[32m aprovado \033[m, parcela será de R$ {fin:.2f} mensais')
else:
    print ('Seu financiamento foi \033[31m reprovado!')
