n = s = c =  0
while True:
    n = int(input("digite um numero: "))
    if n == 999:
        break
    s += n
    c += 1 
print(f"Você digitou {c} valores e a soma deles é {s}")