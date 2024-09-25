# Crie um programa que leia nome, sexo e idade de várias pessoas
# Guarde os dados de cada pessoa em um dicionário e todos em uma lista
# No final mostre:
# Quantas pessoas foram cadastradas?
# Qual é a media de idade?
# Uma lista com as mulheres
# Uma lista com pessoas de idade acima da média
dados_temp = {}
dados = []
idade_acima_avg = []
tot_idade = 0
while True:
    dados_temp["nome"] = str(input("Digite o nome: "))
    dados_temp["sexo"] = str(input("Digite o sexo [M/F]: ")).upper().strip()[0]

    # Validando se a entrada do dado é valida [M/F]
    while dados_temp["sexo"] not in "MF":
        dados_temp["sexo"] = (
            str(input("SEXO INVÁLIDO! TENTE NOVAMENTE! [M/F]: ")).upper().strip()[0])
    dados_temp["idade"] = int(input("Digite a idade: "))

    # Copiando o dicionário dados_temp para a lista dados
    dados.append(dados_temp.copy())

    resp = str(input("Deseja cadastrar outra pessoa? [S/N]")).upper().strip()[0]

    # Validando se a entrada do dado é valida [S/N]
    while resp not in "SN":
        resp = (
            str(input("RESPOSTA INVÁLIDA, TENTE NOVAMENTE! [S/N]")).upper().strip()[0]
        )
    if resp == "N":
        break

# Calculando a média de idade das pessoas cadastradas
for i, v in enumerate(dados):
    tot_idade += dados[i]["idade"]
avg_idade = tot_idade / len(dados)

# Validando se a pessoa tem a idade maior do que a média, caso sim, adicionando-a na lista idade_acima_avg
for i, v in enumerate(dados):
    if dados[i]["idade"] > avg_idade:
        idade_acima_avg.append(dados[i]["nome"])

# Exibindo os resultados
print("-=" * 20)
print(f"Foram cadastrados {len(dados)} pessoas")
print(f"A média de idade foi de: {avg_idade:.2f} anos")
# Exibindo a lista formatada das mulheres
print("As mulheres cadastradas foram :", end=" ")
for p in dados:
    if p["sexo"] == "F":
        print(f"{p['nome']} ", end=" ")
print()
print("As pessoas com idade acima da média: ")
for p in dados:
    if p["idade"] >= avg_idade:
        print("   ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
print()
print("FINAL DO PROGRAMA!!!")
