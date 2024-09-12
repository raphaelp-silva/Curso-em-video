#Aula de tuplas (são imutáveis) ambos os métodos (1, 2 ou 3) chegam ao mesmo resultado
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata-Frita")

# Metodo 1
# for cont in range(0, len(lanche)):
#     print(f"Vou comer {lanche[cont]} na posicao {cont}"")

#Metodo 2 
# for pos, comida in enumerate(lanche):
#     print(f"Eu vou comer {comida} na posicao {pos}")

#metodo 3 
for comida in lanche:
    print(f'Vou comer {comida}')
print("Comi pra caramba")
