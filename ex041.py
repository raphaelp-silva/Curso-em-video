from datetime import date

ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano_nasc

if idade <= 9:
    print(f'O atleta possui {idade} anos, categoria MIRIM')
elif idade <=14:
    print(f'O atleta possui {idade} anos, categoria INFANTIL')
elif idade <= 19:
    print(f'O atleta possui {idade} anos, categoria JUNIOR')
elif idade <=25:
    print(f'O atleta possui {idade} anos, categoria SENIOR')
else:
    print(f'O atleta possui {idade} anos, categoria MASTER')
