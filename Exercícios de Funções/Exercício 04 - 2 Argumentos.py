#Exercício 04
''' Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento 
for positivo, e ‘N’, se seu argumento for zero ou negativo. '''
def validador(numero):
    if numero > 0:
        print('P')
    else:
        print('N')

n = int(input('Digite um número: '))
print('O número é: ', end='')
validador(n)
