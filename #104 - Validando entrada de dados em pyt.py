#104 - Validando entrada de dados em python
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:   
            print('\033[31mERRO! Digite um número inteiro\033[m')
        if ok:
            break
    return valor


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')