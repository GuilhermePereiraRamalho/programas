def metade(preço, formato = False):
    res = preço/2
    return res if formato is False else moeda(res)


def dobro(preço, formato = False):
    res = preço*2
    return res if formato is False else moeda(res)


def aumentar(preço, a=0, formato = False):
    res = preço*(1+(a/100))
    return res if formato is False else moeda(res)


def diminuir(preço,d=0, formato = False):
    res = preço*(1-(d/100))
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:>.2f}'.replace('.',',')


def resumo(preço=0, a=0, d=0):
    print('-'*30)
    print(F'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{a}% de aumento: \t{aumentar(preço,a,True)}')
    print(f'{d}% de redução: \t{diminuir(preço,d,True)}')
