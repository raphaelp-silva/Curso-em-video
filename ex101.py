# Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento
# retornando um valor literal indicando se a pessoa tem o voto negado, opcional ou obrigatório.


def voto(ano_nasc):
    from datetime import date

    ano = date.today().year
    idade = ano - ano_nasc
    if idade < 16:
        return f"Com {idade} anos: NEGADO!"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: OPCIONAL!"
    else:
        return f"Com {idade} anos: OBRIGATÓRIO!"


# Programa principal
nascimento = int(input("Digite o ano de nascimento: "))
print(voto(nascimento))
