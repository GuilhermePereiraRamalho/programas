#92 - Cadastro de trabalhador em python
from datetime import date
cadastro = dict()
trabalhador = list()
hoje = date.today().year

cadastro['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
cadastro['Idade'] = hoje - ano
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['CTPS'] == 0:
    trabalhador.append(cadastro.copy())
else:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salario'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - hoje)
    trabalhador.append(cadastro.copy())
    print('-='*30)
for e in trabalhador:
    for k, v in e.items():
        print(f' - {k} tem o valor {v}')