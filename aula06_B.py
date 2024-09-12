a = input ('Digite qualquer coisa:')

print ('O tipo primitivo desse valor é: ', type(a))
print ('Esse valor só tem espaços?', a.isspace())
print ('Esse valor é um número?', a.isnumeric())
print ('Esse valor é uma letra?', a.isalpha())
print ('Esse valor é alfanumérico?', a.isalnum())
print ('Esse valor está inteiro em caixa alta?', a.isupper())
print ('Esse valor está inteiro em caixa baixa?', a.islower())
