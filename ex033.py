primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

#verificando quem é o maior:
maior = primeiro 
if segundo > maior: 
    maior = segundo
if terceiro > maior:
    maior = terceiro

#verificando quem é o menor:
menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro 


print(f'O maior numero é o {maior}')
print(f'O menor número é o {menor}') 
