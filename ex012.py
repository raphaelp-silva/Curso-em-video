preco = float (input('Digite o valor do produto: R$'))
desc = preco - (preco * 5 / 100)

print(f'O produto custa {preco:.2f}, mas na promoção com desconto de 5% custará {desc:.2f}')
