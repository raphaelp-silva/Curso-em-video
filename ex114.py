# Crie um código em Python que teste se o site do google está acessível pelo computador usado.

import requests

def acessar_site(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        return '\033[31mNão conseguimos acessar o site!\033[m'
    else:
        return '\033[32mConseguimos acessar o site!\033[m'

#Programa principal

teste = acessar_site('https://www.google.com')
print(teste)