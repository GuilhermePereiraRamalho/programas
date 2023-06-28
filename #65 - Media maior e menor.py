#65 - Media maior e menor

i = 's'
maior = 0
soma = 0 
count = 0
menor = 10000000000000000000
while i != 'n':
    n =  int(input('Informe um valor: '))
    i = str(input('deseja contunuar? [s/n] '))
    soma += n
    count += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = soma/count
print('Voce digitou {} números, a media entre eles foi de {}, {} foi o maior valor digitado e {} o menor valor digitado'.format(count, media, maior, menor))
