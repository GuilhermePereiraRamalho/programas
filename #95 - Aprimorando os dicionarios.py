#95 - Aprimorando os dicionarios
dados = dict()
jogador = list()
gols = list()

while True:
    gols.clear()
    total = 0
    dados['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
        total += gols[c]
    dados['gols'] = gols[:]
    dados['total'] = total
    jogador.append(dados.copy())
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if cont in 'nN':
        break 
print('-='*30)
print('cod ', end = '')
for i in dados.keys():
    print(f'{i:<15}', end = '')
print()
print('-'*40)
for k, v in enumerate(jogador):
    print(f'{k:>4} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print() 
print('-'*40)
while True:
    opc = int(input('Mostrar dados de qual jogador? [999 interrompe] '))
    if opc == 999:
        break
    if opc <= len(jogador) - 1:
       print(f'-- LEVANTAMENTO DO JOGADOR {jogador[opc]["Nome"]}')
       for i, v in enumerate(jogador[opc]['gols']):
           print(f'  No jogo {i+1} fez {v} gols')
    if opc >= len(jogador):
        print(f'ERRO! Não existe jogador com código {opc}! Tente novamente')
print('<<< VOLTE SEMPRE >>>')