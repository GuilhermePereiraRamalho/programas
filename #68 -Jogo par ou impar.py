#68 -Jogo par ou impar
from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
result = 0
vit = 0
while True:
    pc = randint(0,10)
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    result = pc + n
    if result % 2 == 0 and pi == 'P':
        print('-'*15)
        print(f'Voce jogou {n}, o computador jogou {pc}. Total de {result} DEU PAR')
        print('-'*15)
        print('Você VENCEU!')
        vit += 1
        print('=-'*15)
        print('Vamos jogar jogavamente:')
    elif result % 2 == 0 and pi == 'I':
        print('-'*15)
        print(f'Você jogou {n}, o computador jogou {pc}. Total de {result} DEU PAR')
        print('-'*15)
        print('VOCÊ PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! VocÊ venceu {vit} vezes')
        break
    elif result % 2 != 0 and pi == 'P':
        print('-'*15)
        print(f'Você jogou {n}, o computador jogou {pc}. Total de {result} DEU IMPAR')
        print('-'*15)
        print('VOCÊ PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! VocÊ venceu {vit} vezes')
        break
    elif result % 2 != 0 and pi == 'I':
        print('-'*15)
        print(f'Voce jogou {n}, o computador jogou {pc}. Total de {result} DEU IMPAR')
        print('-'*15)
        print('Você VENCEU!')
        vit += 1
        print('=-'*15)
        print('Vamos jogar jogavamente:')

