l = float(input('Qual é a largura da parede?'))
a = float(input('Qual é a altura da parede?'))

m2 = l*a 
qte_de_tinta = m2/2

print(f'Sua parede tem {m2:.4} m², será necessário {qte_de_tinta:.4} litros de tinta para pintá-la')
