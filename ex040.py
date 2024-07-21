#programa de media de notas de alunos

nota1 = float(input('Digite a nota da P1: '))
nota2 = float(input('Digite a nota da P2: '))
media = (nota1 + nota2)/2

if media >= 7:
    print(f'Sua média foi {media}, parabéns! \033[32m APROVADO!')
elif media >= 5 < 6.9:
    print(f'Sua média foi {media}, você está de \033[33m RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media}, você foi \033[31m REPROVADO!')
