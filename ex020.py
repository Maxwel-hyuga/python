##Programa exiber um sorteio de uma ordem dentro de uma lista!
from random import shuffle 
n1 = str(input('primeiro nome: '))
n2 = str(input('segundo nome: '))
n3 = str(input('terceiro nome: '))
n4 = str(input('quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentanção do trabalho será: {}'.format(lista))

