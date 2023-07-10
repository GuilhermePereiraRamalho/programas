#113 - Funções aprofundadas em python

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


num1 = leiaInt('Digite um ineiro: ')
num2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')
    