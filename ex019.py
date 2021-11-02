##Programa exiber a escolha de um nome de uma lista!
from random import choice
n1 = input('digite o primeiro nome: ')
n2 = input('digite o segundo nome: ')
n3 = input('digite o terceiro nome: ')
n4 = input('digite o quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O nome escolhido foi {}'.format(escolhido))
