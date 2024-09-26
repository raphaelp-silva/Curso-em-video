# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# Mostre uma mensagem com tamanho adaptável


def escreva(txt):
    print("-" * (len(txt) + 2))
    print(f" {txt}")
    print("-" * (len(txt) + 2))


# programa principal
escreva("Raphael")

escreva("Raphael Paulo da Silva")
