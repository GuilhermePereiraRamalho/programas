#96 - Função que calcula área
def area(l,c):
    a = l * c
    print(f'A área do seu terreno de {l}x{c} é de {a}m²')


print(F'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)