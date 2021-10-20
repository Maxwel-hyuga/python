#Programa converso de medidas!
m = float(input('Digite uma medida em metros: '))
mm = m * 1000
cm = m * 100
dcm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('A medida de {:.0f}m corresponde a: \n{:.0f} milimetros; \n{:.0f} centimetros; \n{:.0f} decimetros; \n{} decametros; \n{} hectametros; \n{} kilometros.'.format(m, mm, cm, dcm, dam, hm, km))

 
