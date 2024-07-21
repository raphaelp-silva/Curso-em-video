d = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos kms você rodou com o carro?'))

preco = (d*60) + (km*0.15)

print(f'Voce devera pagar R${preco:.2f} pelo aluguel do carro, obrigado!')