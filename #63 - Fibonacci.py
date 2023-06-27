#63 - Fibonacci

print('='*20)
print('     FIBONACCI')
print('='*20)

n = int(input('Quantos termos da sequencia de fibonacci voce quer ver? '))
t1 = 0
t2 = 1
print('{} ➝ {}'.format(t1,t2), end = '')
count = 3
while count <= n:
    t3 = t1 + t2
    print('➝ {}'.format(t3), end = '')
    count += 1
    t1 = t2
    t2 = t3
print('➝ FIM')




