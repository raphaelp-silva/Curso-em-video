# Crie um programa que tenha uma função chamada ficha() ,que receba dois parâmetros opcionais.
# O primeiro é o nome de um jogador e o segundo é quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador mesmo com algum dado inválido.


def ficha(nome="<desconhecido>", gol=0):
    print(f"O jogador {nome} fez {gol} gol(s) no campeonato.")


# Programa principal
nome_jogador = str(input("Nome do jogador: "))
gols = input("Número de gols: ")

# Validando se o nome do jogador possui valor
if not nome_jogador:
    nome_jogador = "<desconhecido>"

# Validando se o número de gols é Int, caso seja um valor inválido ele é setado para 0.
if gols.isdigit():
    gols = int(gols)
else:
    gols = 0

# Executando a função
ficha(nome_jogador, gols)
