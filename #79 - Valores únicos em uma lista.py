#79 - Valores únicos em uma lista
valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print('Valor duplicado! Não Vou adicionar...')
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')