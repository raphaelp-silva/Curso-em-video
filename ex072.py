#Criando um programa que lerá o numero digitado pelo usuário e retornará o númeor por extenso (utilizando tuplas)
contagem = ("ZERO", "UM", "DOIS", "TRES", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ",
            "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
resp = "S"
while resp in 'S':
    while True:
        num = int(input("Digite um numero de 0 a 20: "))
        if 0 <= num <= 20:
            break
        print("Tente novamente...", end = '')
    print(f"Você digitou o número {contagem[num]}.")
    resp = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
print("-=-=-= FIM DO PROGRAMA =-=-=-")
