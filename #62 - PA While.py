#62 - PA While


n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
termo=n
v=1
total = 0
mais = 10
while mais !=0:
    total += mais
    while v <= total:
        print('{} ->'.format(termo), end = " ")
        termo += r
        v += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))   
      


