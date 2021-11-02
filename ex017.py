##Programa exiber na tela o calculo do triangulo retângulo!
from math import hypot
ca = float(input('qual a medida do cateto adjacente: '))
co = float(input('qual a medida do cateto oposto: '))
h = hypot(ca, co)
print('O valor do cateto adjacente é {} e o valor do cateto oposto é {}, \nSendo assim sua hipotenusa é {:.2f}'.format(ca, co, h))

