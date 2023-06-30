#78 - Maior e menor na lista
n = list()
maior = menor =  0
for i in range(0,5):
    n.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        menor = n[i]
    elif n[i] < menor:
        menor = n[i]
    if n[i] > maior:
        maior = n[i]
print('=-'*30)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {maior} nas posições ', end ='')
for i in range(0,5):
    if n[i] == maior:
        print(f'{i}...', end = ' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end = '')
for i in range(0,5):
    if n[i] == menor:
        print(f'{i}...', end = ' ')