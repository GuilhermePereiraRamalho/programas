#desenvolva um programa que pergunte a distancia de uma viagem em km e calcule o preço das passagens cobrando 0,50 para ate 200 km e 0,45 para viagens mais longas
nome = input('Seja bem-vindo! Qual seu nome? ')
dist = float(input('{}, qual a distância da sua viagem?'.format(nome)))

if dist <= 200:
    preço = dist * 0.5
    print('{}, o preço da sua passagem para essa viagem de {} km é de R$ {:=.2f}'.format(nome,dist,preço))
else:
    preço = dist * 0.45
    print('{}, o preço da sua passagem para essa viagem de {} km é de R$ {:=.2f}'.format(nome,dist,preço))
