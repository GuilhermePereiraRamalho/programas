#67 - Tabuada 2.0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('=='*21)
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break 
    else:
        print('='*20)
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')