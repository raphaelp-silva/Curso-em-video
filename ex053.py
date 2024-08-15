frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split() #separando a frase em palavras
junto = "".join(palavras) #juntando todas as palavras sem espaço entre elas
inverso = ""
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print("A frase digitada é um palíndromo!")
else:
    print("Não temos um palíndromo!")
