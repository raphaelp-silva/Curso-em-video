print(("-=" * 5), "GERADOR DE PA", ("-=" *5)) 
primeiro = int(input("Digite o primeio termo: "))
razao = int(input("Digite a razao: "))
cont = 1
termo = primeiro
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        cont +=1 
    print("PAUSA")
    mais = int(input("Mais quantos termos você quer? "))
print(f"O programa finalizou e foram mostrados {total} termos!")