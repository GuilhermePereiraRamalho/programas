#102 - Função Fatorial
def fatorial(n, show=False):
    """-> Calcula o fatorial de um número.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('='*25)
    if show:
        for i in range(n,0,-1):
            if i == 1:
                print(f'{i} = ', end = '')
            else:
                print(f'{i} x ', end = '')
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f



print(fatorial(5, show = True))
help(fatorial)