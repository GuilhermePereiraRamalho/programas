#85 - Lista com pares e impares

total = list()
par = list()
impar = list()
for c in range(0,7):
    n = int(input(f'Digite o {c+1}o valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)      
total.append(par[:])
par.clear()
total.append(impar[:])
impar.clear()
print('-='*30)
print(f'O valores pares digitados foram: {sorted(total[0])}')
print(f'O valores impares digitados foram: {sorted(total[1])}')