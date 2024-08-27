# Programa de tabuada! 
# O usuario digitará um valor inteiro positivo e o programa retornará a tabuada ao usuario.
# Número negativo encerra o programa

from time import sleep
while True:
    n = int(input("Digite o valor para calcularmos a tabuada (número negativo para encerrar o programa): "))
    if n < 0:
        break
    print ("-" * 10, f"Tabuada do {n}", "-" *10)
    for c in range (1,11):
        sleep(0.2)
        print(f"{n} x {c} = {n*c}")
    print ("-" * 10, "FIM", "-" *10)
print("Fim do programa tabuada")