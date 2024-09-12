#Criando um programa com uma tupla com os 20 times do campeonato brasileiro, na ordem de colocação, depois mostrando
# - Os 5 primeiros times da classificacao
# - Os ultimos 4 itmes da classificacao
# -  Os times em ordem alfabética.
# - Em que posição está o time da chapecoense.
classificacao = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo',
                 'Bahia', 'Vasco', 'Atlético-MG', 'Internacional', 'Bragantino', 'Athletico-PR',
                 'Juventude', 'Criciúma', 'Grêmio', 'Fluminense', 'Corinthians', 'Vitória', 'Cuiabá', 'Atlético-GO')
print("-=-=-= Os 5 primeiros times são =-=-=-")
print (classificacao[:5])
print("-=-=-= Os ultimos 4 times são =-=-=-")
print (classificacao[-4:])
print ("-=-=-= Times em ordem alfabética =-=-=-")
print (sorted(classificacao))
print("-=-=-= Em qual posição está o Palmeiras? =-=-=-")
print(f"O Palmeiras está em {classificacao.index('Palmeiras')+1}º no campeonato.")