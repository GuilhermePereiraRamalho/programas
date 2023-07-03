#81 - Extraindo dados de uma lista
valores = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    cond = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break
print('-='*15)
valores.sort(reverse= True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valores 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')