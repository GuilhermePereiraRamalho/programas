#60 - fatorial

n = int(input('Informe um número para saber seu fatorial: '))
fat = 1
i = n
'''i = 1
for i in range(1, n+1):
    fat = fat * i
print('{}! = {}'.format(n,fat))'''

while i > 0:
    fat = fat * i
    i -= 1
print('{}! = {}'.format(n,fat))