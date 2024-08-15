idade = 0
maior_idade = 0
mulheres_menos_20 = 0
nome_maior_idade = ""
for p in range (1,5):
    print(f"----- {p}º Pessoa -----")
    name = str(input(f"Nome:")).strip()
    age = int(input(f"Idade: "))
    sexo = str(input(f"Sexo [M/F]: ")).strip()
    idade += age
    if sexo == "f":
        if age <= 20:
            mulheres_menos_20 += 1
    else:
        if age > maior_idade:
            maior_idade = age
            nome_maior_idade = name
idade_media = idade/p
print(f"A idade média do grupo é {idade_media} anos")
print(f"O homem mais velho tem {maior_idade} anos e se chama {nome_maior_idade}")
print(f"Temos {mulheres_menos_20} mulheres com menos de 20 anos.")
