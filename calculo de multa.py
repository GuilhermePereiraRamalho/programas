#faça um programa que leia a velocide de um carro se ele ultrapassar 80 km/h mostre voce foi multado e calcule a multa sendo 7,00 por km acima do limite

vel = float(input('Qual velocidade você está? '))
if vel>80:
    print('VOCÊ FOI MULTADO!!!')    
    multa = (vel-80)*7
    print('O valor da multa é R$ {:=.2f}'.format(multa))
else:
    print('Tenha um bom dia, dirija com seguraça')