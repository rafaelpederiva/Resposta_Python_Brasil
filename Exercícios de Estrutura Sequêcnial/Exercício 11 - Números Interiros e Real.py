#Exercício 11 
'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) O produto do dobro do primeiro com metade do segundo .
b) A soma do triplo do primeiro com o terceiro.
c) O terceiro elevado ao cubo. '''
n1 = int(input('Escreva o primeiro número inteiro: '))
n2 = int(input('Escreva o segundo número inteiro: '))
n3 = float(input('Escreva o primeiro número real: '))
print('O dobro do primeiro resultado é:', (n1*2), 'A metade do segundo é', (n2/2))
print('A soma do triplo do primeiro número inteiro com o real é:', (n1*3)+n3)
print('O valor ao cubo do terceiro é:', n3**3)