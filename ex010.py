v1 = float(input('Quantos reais você tem na carteira? R$'))
vd = 3.27
vf = v1/vd 

print(f'Com R$ {v1:.2f}, voce consegue comprar US${vf:.2f} na cotacao atual, que é de {vd} reais.')