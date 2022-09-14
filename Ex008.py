#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n=float(input('Digite uma distância em metros:'))
cm = n*100
mm = n*1000
print('A distância em metros é {} m\n A distância em centimetros é {} cm\n A distância em Milimetros é {} mm'.format(n,cm,mm))