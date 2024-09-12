v = int(input("Qual é a velocidade do carro? :"))
vel_per = 80
if v <= 80:
    print("Você está dentro da velocidade permitida, parabéns!")
else:
    dif = v - vel_per
    multa = dif * 7
    print(
        f"Você está trafegando a {v}km/h, isso está acima do limite de velocidade! Você foi multado em R${multa:.2f}reais "
    )
print("Boa viagem!")
