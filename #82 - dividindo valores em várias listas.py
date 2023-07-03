#82 - dividindo valores em várias listas
valores = list()
pares = list()
impares = list()

while True:
    n = int(input('Digite um numero: '))
    valores.append(n)
    cond = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break
for i in range(0,len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])
print('-='*15)
print(f'A Lista completa é {valores}')
print(f'A Lista de pares é {pares}')
print(f'A Lista de impares é {impares}')