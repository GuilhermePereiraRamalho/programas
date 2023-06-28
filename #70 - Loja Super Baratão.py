#70 - LEstatísticas em produtos
soma = tot_m = menor_p = count = 0
nome_m = ''
print('-'*30)
print('      LOJA SUPER BARATÃO   ')
print('-'*30)

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    count += 1
    soma += preço
    if preço > 1000:
        tot_m += 1
    if  count == 1 or preço < menor_p:
        menor_p = preço
        nome_m = nome
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('{:=^20}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {soma}')
print(f'Temos {tot_m} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_m} que custa R$ {menor_p}')
