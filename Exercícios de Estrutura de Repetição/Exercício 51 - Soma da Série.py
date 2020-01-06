#Exercício 51 
'''Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.'''
print('S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. ')
termos = int(input('Digite n: '))
n1 = 1
n2 = 1
lista_n1 = []
lista_n2 = []
print('\nS = ', end=' ')
for i in range(termos):
    print('%i/%i' %(n1,n2),end='')
    lista_n1.append(n1)
    lista_n2.append(n2)
    if n1 == termos:
        print(' => ', end='')
    else:
        print(' + ', end='')
    n1 += 1
    n2 += 2
print('%i/' %sum(lista_n1) + '%i' %sum(lista_n2) +'\n')