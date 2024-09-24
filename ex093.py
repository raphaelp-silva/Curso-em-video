# Crie um programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas ele jogou
# Depois vai ler a quantidade de gols feitos em cada partida
# No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos no campeonato
infos = {}
gols = []
# Lendo o nome do jogador e quantos jogos ele jogou
infos["nome"] = str(input("Nome do jogador: "))
jogos = int(input(f"Quantas partidas {infos['nome']} jogou? "))

# Criando um looping para ler quantos gols o jogador fez por jogo
for i in range(0, jogos):
    gol_jogo = int(input((f"Quantos gols {infos['nome']} fez no jogo {i}? ")))

    # Adicionando o numero de gols na lista gols
    gols.append(gol_jogo)

# Adicionando a lista gols ao dicionário infos
infos["gols"] = gols[:]

# Somando e adicionando o total de gols ao dicionário
infos["total"] = sum(gols)

# Exibindo o resultado de 3 maneiras diferentes
print("-=" * 20)
# Maneira 1:
print(infos)
print("-=" * 20)

# Maneira 2:
for k, v in infos.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 20)

# Maneira 3:
print(f"O jogador {infos['nome']} jogou {jogos} partidas")
for i, v in enumerate(infos["gols"]):
    print(f" =>  Na partida {i} fez {v} gols")
print(f"Fez um total de {sum(gols)} gols")

print("\n FIM DO PROGRAMA!")
