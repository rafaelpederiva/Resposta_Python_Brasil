#Exercício 09 
''' Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9). '''
farenheit = int(input('Informe a temperatura em Farenheit: '))
celsius = 5 * (farenheit - 32) / 9.0
print('A temperatura em Celsius eh', celsius)