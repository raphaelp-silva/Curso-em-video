salario = float(input('Qual é o valor do seu salário?: R$'))

if salario <= 1250: 
    novo_salario = salario*1.15 #ou podemos usar (salario + (salario * 15 /100) para achar a porcentagem de aumento ou um possivel desconto por exemplo)
else:
    novo_salario = salario*1.10 # ou salario + (salario * 10 / 100) para achar a porcentagem de aumento ou um possivel desconto.

print(f'O seu novo salário é de {novo_salario:.2f}')
