#101 - Funções para votação
from datetime import date
def voto(idd):
    if 16 <= idd < 18 or idd > 65:
        print(f'Com {idd} anos: VOTO OPCIONAL')
    elif idd < 16:
        print(f'Com {idd} anos: NAO VOTA')
    else:
        print(f'Com {idd} anos: VOTO OBRIGATÓRIO')


#programa principal
hoje = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = hoje - ano
voto(idade)