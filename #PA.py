#PA

n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
d = n + (10 - 1) * r
for i in range(n,d+r,r):
   print(i)