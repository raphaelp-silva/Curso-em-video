# Criar um programa que leia o nome e o preço de varios produtos
# O programa deverá perguntar quando o usuario quiser parar, e no final mostrar
# qual é o total gasto na compra/ quantos produtos custaram mais de 1000 reais e
# # qual é o produto mais barato comprado
total = produto_mil = cont = menor_preco = 0
produto_barato = " "
while True:
    nome_produto = str(input("Nome do produto: "))
    preco_produto = float(input("Preço: "))
    cont += 1
    total += preco_produto
    if preco_produto >= 1000:
        produto_mil += 1
    if cont == 1 or preco_produto < menor_preco:
        menor_preco = preco_produto
        produto_barato = nome_produto
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if continuar == "N":
        break
print("-=" * 10, "FIM DO PROGRAMA", "-=" * 10)
print(f"Sua compra deu um TOTAL de {total:.2f} reais")
print(f"O Produto mais barato foi {produto_barato} e custou R$ {menor_preco:.2f}")
print(f"Voce comprou {produto_mil} produtos acima de mil reais.")
