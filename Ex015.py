#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
dia = int(input('Quantos dias você pretende ficar com o carro?'))
km = float(input('Quantos KM você andou com o carro?'))
p = 60*dia + 0.15*km

print('Você ficou {} dias com o carro e andou {:.2f}km, seu preço de aluguel será R${}'.format(dia,km,p))