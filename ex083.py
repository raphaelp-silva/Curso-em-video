#Criar um programa que leia a entrada do usuário (com parênteses) e diga se é uma expressão válida ou inválida
expressao = str(input("Digite a sua expressão: "))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão é Válida!")
else:
    print("sua expressão não é Válida!")
