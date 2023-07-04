#85 - Lista com pares e impares

total = [[], []]

for c in range(0,7):
    n = int(input(f'Digite o {c+1}o valor: '))
    if n % 2 == 0:
        total[0].append(n)
    else:
        total[1].append(n)      

print('-='*30)
print(f'O valores pares digitados foram: {sorted(total[0])}')
print(f'O valores impares digitados foram: {sorted(total[1])}')