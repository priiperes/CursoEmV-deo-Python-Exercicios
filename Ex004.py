#Faça um programa que leia algo pelo teclado  e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.
n=input('Dígite qualquer coisa ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaço?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?',n.isalpha())
print('É alfanumérico',n.isalnum())
print('É tudo maíusculo?', n.isupper())
print('É tudo minusculo?',n.islower())
print('É imprimivel?', n.isprintable())
