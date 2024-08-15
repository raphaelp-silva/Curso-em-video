from datetime import date
maioridade = 0
menoridade = 0
ano = date.today().year
for pess in range (1,8):
    nascimento = int(input(f"Qual é o ano do nascimento da {pess}º pessoa?"))
    idade = ano - nascimento
    if idade >= 21:
        maioridade += 1
    else:
        menoridade +=1
print(f"No total tivemos {menoridade} menores de idade e {maioridade} maiores.")
