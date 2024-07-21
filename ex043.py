peso = float(input("Qual é o seu peso atual em KG?"))
altura = float(input("Qual é a sua altura? "))
imc = peso / (altura**2)

if imc < 18.5:
    print(f"O seu IMC é {imc:.1f}, você está ABAIXO do peso ideal")
elif 18.5 <= imc < 25:
    print(f"O seu IMC é {imc:.1f}, você está DENTRO do peso ideal")
elif 25 <= imc <= 29.9:
    print(f"O seu IMC é {imc:.1f}, você está com SOBREPESO")
elif 30 <= imc <= 34.9:
    print(f"O seu IMC é {imc:.1f}, você está COM OBESIDADE GRAU 1")
elif 35 <= imc <= 39.9:
    print(f"O seu IMC é {imc:.1f}, você está COM OBESIDADE GRAU 2")
else:
    print(f"O seu IMC é {imc:.1f}, você está COM OBESIDADE EXTREMA")
