# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep

print('-='*15)
print('    CALCULADORA DE AUMENTO'    )
print('-='*15)

#importando dados de salario
nome = input('Qual seu nome: ')
sleep(2)
print('{}, muito prazer em te conhecer, seja bem-vindo(a)!'.format(nome))
sal = float(input('{}, me informe seu salário: R$ '.format(nome)))
print('Calculando...')
sleep(3)

#calculo de aumento
if sal <= 1250:
    aumento = sal * 0.15
    novo_sal = sal * 1.15
else:
    aumento = sal  *0.1
    novo_sal = sal * 1.1  

print('{}, seu aumento será de R$ {:=.2f}, sendo assim, seu novo salário será de R$ {:=.2f}'.format(nome, aumento, novo_sal))  
