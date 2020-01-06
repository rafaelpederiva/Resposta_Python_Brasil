#Exercício 34 
'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível 
apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot = tot + 1        
if tot == 2:
    print('O número é PRIMO!')
else:
    print('O número não é PRIMO!')