## Faça um programa que leia um angulo e mostre na tela o valor do seno cosseno e tangente desse angulo

import math

ang = float(input('Informe um ângulo em ºC: '))
ang_rad = math.radians(ang)
sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tg = math.tan(ang_rad)
print('O sen {:.2f} ºC vale {:.2f}, o cos {:.2f} ºC vale {:.2f} e a tan {:.2f} ºC vale {:.2f}'.format(ang,sen,ang,cos,ang,tg))