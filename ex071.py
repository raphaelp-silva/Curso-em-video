# Criando um programa que simula o funcionamento de um caixa eletronico
# o usuario digitará o valor a ser sacado e o programa retorna quantas cédulas 
# de cada valor serão entregue (R$1, R$10, R$20 ou R$50)
print("=" *20, "Banco ABCD", "=" * 20)
valor_saque = int(input("Qual valor você quer sacar? R$ "))
total = valor_saque
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"Total de {total_ced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print("=" * 50)
print("Obrigado! Volte sempre ao ABCD bank")