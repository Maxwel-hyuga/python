##Programa que exibe desconto no produto!

p = float(input('Qual é o preço do produto: R$'))
d = p - (p * 0.05)
print('O produto que custava R${:.2f}, na promoção de 5% vai sair há R${:.2f}'.format(p, d))

