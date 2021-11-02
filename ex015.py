#Programa exibe calculos de aluguel de carros!

dias = int(input('Quantos dias de aluguel: '))
km = int(input('Quantos kilometros rodados: '))
vd = 60
vkm = 0.15
total = dias * vd + km * vkm
print('Dias utilizados: {}'.format(dias))
print('Kilometros rodados: {}'.format(km))
print('O valor total a pagar pelo aluguel do veículo é: R${} reais'.format(total))
