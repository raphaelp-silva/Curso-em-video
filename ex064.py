num = int(input("Digite o número que deseja: "))
cont = 0
soma = num
while num != 999:
    num = int(input("Digite outro valor: "))
    cont +=1 
    soma += num 
soma = soma - 999 
print(f"Fim! você digitou {cont} valores e a soma deles é {soma}")