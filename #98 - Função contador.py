#98 - Função contador
from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        print('ERRO! Impossivel contatar com passo 0, vou fazer uma contagem com passo 1')
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end = '', flush = True)
            cont += p
            sleep(.2)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end = '', flush = True)
            cont -= p
            sleep(.2)
        print('FIM!')       


contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)