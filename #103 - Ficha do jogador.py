#103 - Ficha do jogador
def ficha(nome ='', gols = 0):
    print('='*30)
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no capeonato')


#programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n,g)
