from datetime import date

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano_nascimento
idade_alistamento = 18

if idade < idade_alistamento:
    print(f'Você ainda é juvenil, faltam {idade_alistamento - idade} anos para você se alistar!')
elif idade > idade_alistamento:
    print(f'Você já é veterano, já deveria ter se alistado há {idade - idade_alistamento} anos!')
else:
    print(f'Você tem {idade} anos, está na hora de virar homem e se alistar!')
