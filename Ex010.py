# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e quantos dolares ela pode comprar.
#US$1,00 = R$3,27
real=float(input('Digite quanto dinheiro você tem? R$'))
dolar=real/3.27
print('Convertendo R${:.2f} em dolares daria US${:.2f}'.format(real, dolar))

