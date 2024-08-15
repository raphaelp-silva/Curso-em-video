resp = "S"
soma = quant = media = maior_numero = menor_numero = 0
while resp in "Ss":
    num = int(input("Digite o número: "))
    soma += num
    quant += 1
    if quant == 1:
        menor_numero = maior_numero = num
    else:
        if num > maior_numero:
            maior_numero = num
        if num < menor_numero:
            menor_numero = num
    resp = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
media = soma / quant 
print(f"Você digitou {quant} números e a média deles é {media}")
print(f"O maior valor digitado foi o {maior_numero} e o menor foi {menor_numero}")