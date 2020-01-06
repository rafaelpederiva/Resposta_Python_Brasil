#Exercício 23 
'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar
também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de 
testes (divisões) executados.'''
lista_primos = []
numero = int(input('Digite até que número quer saber se é primo: '))
for i in range(1,numero + 1):
    cont = 0
    for c in range(1, i + 1):
        if i % c == 0:
            cont += 1
    if cont <= 2:
        lista_primos.append(i)
print('A sequencia de números primos são: ')
print(lista_primos)