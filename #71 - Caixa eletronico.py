#71 - Caixa eletronico


print('='*30)
print('{:^30}'.format('BANCO CEV') )
print('='*30)
v = int(input('Que valor você quer sacar? R$ '))
total = v
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('VOLTE SEMPRE AO BANCO CEV. TENHA UM BOM DIA!')