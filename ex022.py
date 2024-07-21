nome = str(input('Digite o seu nome: '))
print (nome.upper()) #transformando todos os caracteres em maiusculos
print (nome.lower()) # transformando todos os caracteres em minusculos
print (len(nome.strip())) #contando os caracteres sem considerar os espacos no inicio e no fim 

dividido = nome.split() # separando o nome em blocos 
print (len(dividido[0])) # contando os caracteres do bloco 0, no caso, o primeiro nome
