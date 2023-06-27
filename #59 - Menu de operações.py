#59 - Menu de operações
from time import sleep

n1 = float(input('Informe um valor: '))
n2 = float(input('Informer outro valor: '))

print('-='*15)
print('      MENU DE OPERAÇÕES'    )
print('-='*15)

escolha = 0

while escolha != 5:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    escolha = int(input('\nSelecione uma opção: '))
    if escolha == 1:
        soma = n1 + n2
        print('\n{} + {} = {}\n'.format(n1, n2, soma))
    elif escolha == 2:
        mult = n1 * n2
        print('\n{} X {} = {}\n'.format(n1, n2, mult))
    elif escolha == 3:
        if n1 > n2:
            print('\nO maior entre os números digitados é: {}\n'.format(n1))
        else:
            print('\nO maior entre os números digitados é: {}\n'.format(n2))
    elif escolha == 4:
        n1 = float(input('Digite um novo numero: '))
        n2 = float(input('Digite outro novo numero: '))
print('FINALIZADO...')
sleep(1.5)
print('OBRIGADO POR UTILIZAR NOSSO PROGRAMA, TENHA UM BOM DIA!')