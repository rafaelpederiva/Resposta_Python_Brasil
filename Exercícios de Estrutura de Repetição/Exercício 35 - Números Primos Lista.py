#Exercício 35 
'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número 
inteiro informado pelo usuário.'''
def num_primos(n):
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    return divisores == 2
num = int(input("Digite um número: "))
print('\nTodos os números primos até %d número são: '%num)
for n in range(1, num + 1):
    if num_primos(n):
        print(n, end=' ')
print('\n')