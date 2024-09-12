# Criar um programa com uma tupla unica com nomes de produtos e seus respectivos preços
# No final, mostrar uma listagem de preços, organizando os dados em forma tabular.
lista_produtos = (
    "Lápis",
    3,
    "Borracha",
    1,
    "Caderno",
    15,
    "Estojo",
    10.90,
    "Mochila",
    125.90,
)
print("=-" * 40)
print("LISTA DE PRODUTOS E PREÇOS")
print("=-" * 40)
for pos in range(0, len(lista_produtos)):
    if pos % 2 == 0: #todos os produtos estão nas posicoes pares 
        print(f"{lista_produtos[pos]:.<30}", end="")
    else:
        print(f"R${lista_produtos[pos]:>7.2f}")
