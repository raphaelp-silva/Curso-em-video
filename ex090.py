#Criar um programa que leia nome e média de um aluno, guardando-o em um dicionário.
#Ao final, mostrar o conteúdo da estrutura na tela.
dados = {}
dados['nome'] = str(input("Digite o nome do aluno: "))
dados['média'] = float(input(f"Qual foi a média do {dados['nome']} : "))

#Validando a situação da média do aluno 
if dados['média'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados['média']:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Reprovado'

#exibindo os resultados
print('-=' * 20)
for k, v in dados.items():
    print(f" - {k} é igual a {v}")
