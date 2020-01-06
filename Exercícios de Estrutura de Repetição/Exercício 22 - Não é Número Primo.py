#Exercício 22 
#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é primo!')
    for i in range(1, num + 1):
        if (num % i == 0):
            print('Ele é divisível por: \033[33m',i,'\033[m')