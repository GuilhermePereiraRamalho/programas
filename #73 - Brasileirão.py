#73 - Brasileirão

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro','Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense','Sport', 'Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')

print('-='*30)
print(f'Lista de times do brasileirão {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*30)
print(f'Os 4 ultimos são: {times[16:20]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
print('O Chapecoense esta na {} ª posição'.format(times.index('Chapecoense')+1))
