##Programa calcula quantidade de tinta para pintar uma parede!

l = float(input('Largura da parede:'))
A = float(input('Altura da parede: '))
a = l * A
t = a / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(l, A, a))
print('Para pintar essa parede, você precisará de {:.2f} litros  de tinta.'.format(t))
