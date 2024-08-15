sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Sexo inválido, digite novamente: ")).strip().upper()[0]
print(f"Você digitou {sexo}, sexo registrado com sucesso!")