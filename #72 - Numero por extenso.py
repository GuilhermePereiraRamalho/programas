#72 - Numero por extenso
num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

cont = int(input('Digite um numero entre 0 e 20: '))
if cont not in num:      
    while cont not in num:
        cont = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
for i in range (0,21):
    if cont == num [i]:
        print(f'Voce digitou o número {ext[i]}')