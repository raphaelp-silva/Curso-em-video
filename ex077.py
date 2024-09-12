# Crie um programa que tenha uma tupla com varias palavras(sem acentos).
# Mostrar para cada palavra quais sao as suas vogais
palavras = ('Lapis', 'Caneta', 'Caderno', 'Lousa', 'Mochila')
for p in palavras: #esse for analisa cada elemento dentro da tupla
    print(f"\n Na palavra {p.upper()} temos ", end =' ')
    for letra in p: #esse for analisa cada letra da palavra dentro da tupla
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
