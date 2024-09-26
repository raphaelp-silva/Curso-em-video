# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores int.
# Seu programa deve analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* num):
    cont = maior = 0
    print("-=" * 30)
    sleep(0.5)
    print("ANALISANDO OS VALORES PASSADOS...")
    for n in num:
        print(f"{n} -> ", end="", flush=True)
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1

    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"\nO maior número é o {maior}")


# Programa principal

maior(-15,12,24,33,39,41,64)
maior(-2)