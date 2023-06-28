## Faça um programa que leia um valor em metros e exima convertido em cm e mm

nome = input('Olá, tudo bem? Qual seu nome? ')
m = float(input('Certo, {}, informe um medida em metros: '.format(nome)))
cm = m * 100
mm = m * 1000
print('{}, essa media que você digitou de {} m, equivale à {} cm e à {} mm'.format(nome,m,cm,mm))