# Crie uma programa com uma função chamada area() que receba as dimensões de um terreno retangular
# e mostre a área do terreno
def area(l, c):
    tam = l * c
    print(f"O terreno tem as dimensões {l} x {c} que resulta em {tam} m².")


def linha():
    print("-=" * 20)
    print("          METRAGEM DE TERRENO")
    print("-=" * 20)


# Programa principal
largura = float(input("Digite a largura do seu terreno (m): "))
comprimento = float(input("Digite o comprimento do seu terreno (m): "))
linha()
area(largura, comprimento)
print("\nFIM!")
