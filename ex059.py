n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opcao = 0

while opcao != 5:
    print(("""\n
            ================ MENU ================
            [1]\tSOMAR
            [2]\tMULTIPLICAR
            [3]\tMAIOR
            [4]\tNOVOS NÚMEROS
            [5]\tSAIR
            => """))
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print(f"A soma dos valores resulta {n1+n2}")
    elif opcao == 2:
        print(f"A multiplicação dos valores resulta em {n1 * n2}")
    elif opcao == 3:
        if n1 > n2:
            maior_valor = n1
        else:
            maior_valor = n2
        print(f"O maior valor entre eles é {maior_valor}")
    elif opcao == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        break
    else:
        print("Opcao invalida, tente novamente...")
print("Obrigado! até logo!")
