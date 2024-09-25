# Aprimore o ex93 para que ele funcione com vários jogadores
# Incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
infos = {}
jogadores = []
gols = []
while True:
    infos.clear()
    # Lendo o nome do jogador e quantos jogos ele jogou
    infos["nome"] = str(input("Nome do jogador: "))
    jogos = int(input(f"Quantas partidas {infos['nome']} jogou? "))

    # Criando um looping para ler quantos gols o jogador fez por jogo
    for i in range(0, jogos):
        gol_jogo = int(input((f"Quantos gols {infos['nome']} fez no jogo {i+1}? ")))

        # Adicionando o numero de gols na lista gols
        gols.append(gol_jogo)

    # Adicionando a lista gols ao dicionário infos
    infos["gols"] = gols[:]
    # Somando e adicionando o total de gols ao dicionário
    infos["total"] = sum(gols)
    jogadores.append(infos.copy())
    gols.clear()
    while True:
        resp = str(input("Deseja cadastrar outro jogador? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S/N")
    if resp == "N":
        break

# Exibindo os resultados
print("-" * 30)
# Criando o cabeçalho
print("COD ", end="")
for i in infos.keys():
    print(f"{i:<15}", end="")
print()
print("-=" * 20)

# Exibindo a lista de jogadores 
for k, v in enumerate(jogadores):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
# Criando a sessão de consulta de datalhes por jogador
while True:
    busca = int(
        input("De qual jogador você quer visualizar os dados? (999 para parar): ")
    )
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"ERRO! Não existe jogados com o código {busca}. Tente novamente!")
    else:
        print(f" --- LEVANTAMENTO DOS DADOS DO JOGADOR {jogadores[busca]['nome']}:")
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f"   No jogo {i+1} fez {g} gols")
    print("-" * 40)
print("\n FIM DO PROGRAMA!")
