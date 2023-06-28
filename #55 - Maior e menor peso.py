#55 - Maior e menor peso

maior_peso = 0
menor_peso = 0

for i in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('Dentre essas 5 pessoas o maior peso é de {} kg, e o menor peso é de {} kg'.format(maior_peso, menor_peso))
