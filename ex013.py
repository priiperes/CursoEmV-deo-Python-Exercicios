#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s=float(input('Qual o seu salário atual? R$'))
sa=s*(1.15)
print('Seu salário era de R${}, e agora com aumento será de R${:.2f}'.format(s,sa))
