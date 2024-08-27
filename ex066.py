# Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando voce digitar 999, que é a condicao de parada
# No final, mostre quantos numeros foram digitados e a soma entre eles.

n = s = c =  0
while True:
    n = int(input("digite um numero: "))
    if n == 999:
        break
    s += n
    c += 1 
print(f"Você digitou {c} valores e a soma deles é {s}")