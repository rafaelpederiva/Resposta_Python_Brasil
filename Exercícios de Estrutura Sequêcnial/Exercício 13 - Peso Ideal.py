#Exercício 13 
'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7 '''
print('Cálculo de peso ideal')
print('*************************')
sexo = input('Informe o seu sexo (M/F): ')
altura = float(input('Informe agora sua altura: '))
peso = float(input('Agora informe o seu peso: '))
if sexo == ('M'):
    pesoIdeal = (72.7*altura) - 58
else:
    pesoIdeal = (62.1*altura) - 44.7
if peso > pesoIdeal:
    print('Você está acima de seu peso, seu peso ideal é:', pesoIdeal)
elif peso < pesoIdeal:
    print('Você está abaixo do peso, seu peso ideal é:', pesoIdeal)
else:
    print('Você está em seu peso ideal!')