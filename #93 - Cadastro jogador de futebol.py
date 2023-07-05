#93 - Cadastro jogador de futebol
dados = dict()
jogador = list()
gols = list()
total = 0
dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total += gols[c]
dados['gols'] = gols[:]
dados['total'] = total
print('-='*30)
print(dados)
print('-='*30)
jogador.append(dados.copy())
for e in jogador:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {dados["Nome"]} fez {partidas} partidas:')
for c in range(0,partidas):
    print(f'   => Na partida {c+1}, fez {gols[c]} gols')
print(f'Foi um total de {total} gols.')