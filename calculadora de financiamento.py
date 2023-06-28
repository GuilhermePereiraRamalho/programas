#Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. o programa vai perguntar o vaor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela nao pode exceder 30% do salario ou o emprestimo será negado
from time import sleep
cores= {'limpa': '\033[m',
        'red': '\033[1;31m',
        'green': '\033[1;32m'}

#inicio
print('-='*20)
print('      CALCULADORA DE FINANCIAMENTO   ')
print('-='*20)
sleep(2)

#input de dados

print('SEJA MUITO BEM VINDO AO AMBIENTE DE FINANCIAMENTO')
sleep(2)
nome = input('POR GENTILEZA ME INFORME SEU NOME: ')

print('MUITO PRAZER EM TE CONHECER, {}'.format(nome.upper()))
sleep(2)
val_casa = float(input('{}, ME INFORME O VALOR DA CASA QUE VOCÊ DESEJA FINANCIAR: R$'.format(nome.upper())))
sal = float(input('PERFEITO, {}, AGORA ME INFORME SEU SALÁRIO POR GENTILEZA: R$'.format(nome.upper())))
anos = float(input('CERTO, AGORA ME INFORME EM QUANTOS ANOS VOCÊ PRETENDER PAGAR ESSE VALOR DA CASA: '))
sleep(1)
print('CALCULANDO...')
sleep(3)
#calculos
parcela = val_casa / (anos*12)
if parcela <= (sal*0.3):
    print('{}, SEU FINANCIAMENTO FOI {}APROVADO{}, SUA CASA NOVA CUSTARA PARA VOCÊ R$ {:=.2f} POR MÊS AO LOGO DE {} ANOS'.format(nome.upper(),cores['green'], cores['limpa'], parcela, anos))
else:
    print('{}, SEU FINANCIAMENTO FOI {}REPROVADO{}'.format(nome.upper(),cores['red'], cores['limpa']))