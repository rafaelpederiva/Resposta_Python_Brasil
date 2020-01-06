#Exercício 32 
'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser 
conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''
num = int(input("Digite um número: "))
lista = []
lista.append(num)
fatorial = num
i = num
while i != 1:
  i -= 1
  fatorial = fatorial * i
  lista.append(i)
print('!%d' %num, end=' = ')
for x in lista:
    print( x , end='')
    if x == 1:
        print(end=' = ')
    else:
        print(end=' . ')
print(fatorial)