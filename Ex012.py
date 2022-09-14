#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p=float(input('Qual o preço do produto ? R$'))
pd=p*(0.95)
print('O preço do produto é R${}, seu preço com desconto de 5% é R${:.2f}'.format(p,pd))