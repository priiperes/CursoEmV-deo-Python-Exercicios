#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
l=float(input('Dígite a largura da parede em metros: '))
c=float(input('Dígite o comprimento da parede em metros:'))
a=l*c
print('A área é: {} m² \nSerá preciso {} latas de tinta.'.format(a,a/2))