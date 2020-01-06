#Exercício 49 
'''Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. '''
print('S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. ')
termos = int(input('Digite n: '))
n1 = 1
n2 = 1
print('\nS = ', end=' ')
for i in range(termos):
    print('%i/%i' %(n1,n2),end='')
    if n1 == termos:
        print('')
    else:
        print(' + ', end='')
    n1 += 1
    n2 += 2
