#75 - Analise de dados de em uma tuplas
num = (int(input('Informe um valor: ')), int(input('Informe outro valor: ')),
       int(input('Informe outro valor: ')), int(input('Informe outro valor: ')))  
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma das posições')
print('Os valores pares digitados foram ', end ='')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')