# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastro-o (com a idade) em um dicionário.
# Se a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar.
from datetime import date

dados = {}
# Recebendo dados para preencher o dicionário
dados["nome"] = str(input("Nome: "))
ano_nascimento = int(input("Ano de nascimento: "))
# Calculando a idade da pessoa cadastrada com base no ano da máquina
idade = (date.today().year) - ano_nascimento
dados["idade"] = idade
ctps = int(input("Carteira de trabalho (0 caso não tenha): "))
# Validando se a pessoa cadastrada possui CTPS ou não
if ctps == 0:
    pass
else:
    dados["ctps"] = ctps
    dados["Ano de contratação"] = int(input("Ano de contratação: "))
    dados["salario"] = float(input("Salário: R$"))
    # Calculando o tempo de contribuicao com base no ano da máquina
    tempo_contribuicao = (date.today().year) - dados["Ano de contratação"]
    # Calculando o tempo restande de trabalho da pessoa cadastrada
    tempo_restante = 35 - tempo_contribuicao
    idade_para_aposentar = idade + tempo_restante
    # adicionando o resultado desse calculo ao dicionário
    dados["aposentadoria"] = idade_para_aposentar
print("-=" * 30)
# Exibindo os dados cadastrados com os resultados processados
for k, v in dados.items():
    print(f"- {k} tem o valor {v}")
print("\n FIM DO PROGRAMA!!!")
