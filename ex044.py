print ("========== LOJAS DA SILVA ==========")
valor_compra = float(input("Digite o valor da sua compra R$ "))
print ('''Escolha uma das opções de pagamento abaixo
       [1] à vista com DINHEIRO ou CHEQUE
       [2] à vista no CARTÃO DE CRÉDITO
       [3] 2x no CARTÃO DE CRÉDITO
       [4] 3x ou mais no CARTÃO DE CRÉDITO''')
opcao = int(input("Digite a opção de sejada: "))
if opcao == 1:
    valor_final = valor_compra*0.9 
    print(f"Você ganhou desconto, sua compra sairá por R$ {valor_final}")
elif opcao == 2:
    valor_final = valor_compra*0.95
    print(f"Você ganhou desconto, sua compra sairá por R$ {valor_final}")
elif opcao == 3:
    valor_final = valor_compra
    print(f"Sua compra sairá por R$ {valor_final}")
elif opcao == 4:
    parcelas = int(input("Em quantas parcelas?"))
    valor_final = valor_compra*1.20
    valor_final_parcelado = valor_final/parcelas
    print(f"Você pagará R$ {valor_final} em {parcelas} parcelas de {valor_final_parcelado} reais, obrigado!")
else:
    print("Opcão invalida!")
