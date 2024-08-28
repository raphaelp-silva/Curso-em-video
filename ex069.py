# Crie um programa que leia e cadastre a idade e o sexo de varias pessoas
# o programa deverá perguntar se o usuario quer continuar e ao fim do programa 
# deverá exibir quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e 
# quantas mulheres tem menor de 20 anos

homens = pessoas_maior_18 = mulher_menor_20 = 0
while True:
    print("-" *10, "Cadastre uma pessoa", "-"*10)
    idade = int(input("Qual é a idade: "))
    sexo = ' '
    while sexo not in 'HM':
        sexo = str(input("Qual é o sexo [H/M]: ")).upper().strip()[0]
    if sexo == "H" and idade >= 18:
        homens += 1
        pessoas_maior_18 += 1
    elif sexo == "H" and idade < 18:
        homens += 1
    elif sexo == "M" and idade > 20:
        pessoas_maior_18 +=1 
    elif sexo == "M" and idade >= 18 < 20:
        mulher_menor_20 += 1
        pessoas_maior_18 +=1
    elif sexo =="M" and idade < 18:
        mulher_menor_20 += 1
    control = ' '
    while control not in 'SN':
        control = str(input("Deseja cadastrar outra pessoa? [S/N]")).upper().strip()[0]
    if control == "N":
        break
print("Fim do programa!!!")
print ("=-" * 20)
print(f"O programa leu {homens} homens, {pessoas_maior_18} pessoas com mais de 18 anos e {mulher_menor_20} mulheres com menos de 20 anos")
