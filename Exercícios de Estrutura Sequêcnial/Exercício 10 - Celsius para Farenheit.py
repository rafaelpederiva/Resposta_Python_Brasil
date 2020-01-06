#Exercício 10 
#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
celsius = int(input('Informe a temperatura em Celsius: '))
farenheit = ((celsius / 5.0) * 9.0) + 32.0
print('A temperatura em Farenheit eh', farenheit)