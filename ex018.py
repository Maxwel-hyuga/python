##Programa exiber calculo do seno, cosseno, tangente!
from math import sin, cos, tan, radians
a = float(input('Qual a medida do angulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O angulo {}, seu seno é {:.2f}º'.format(a, seno))
print('O angulo {}, seu consseno {:.2f}º'.format(a, cosseno))
print('O angulo {}, sua tangente {:.2f}º'.format(a, tangente))


