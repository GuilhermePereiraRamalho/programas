#Crie um programa que leia o nome completo de uma pessoa e mostra: O nome todo em maiusculas, o nome todo em minusculas, quantas letres tem sem contar espaços e quantas letras tem no primeiro nome.
print('{:=^50}'.format('ANALISADOR DE NOMES'))
nome = str(input('Digite seu nome completo: ')).strip()
quebrado = nome.split()
print('Olá {}, muito prazer!'.format(nome))
print('''Seu nome em maiusculas é: {}
Seu nome em minúsculas é: {}
Seu nome completo possui {} letras
Seu primeiro nome possui {} letras'''.format(nome.upper(),nome.lower(),len(nome)-nome.count(' '),len(quebrado[0])))