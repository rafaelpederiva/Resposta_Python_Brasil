#Exercício 07 
#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
lista = []
mult = 1
for i in range(0,5):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    mult = mult * numero
print('A lista é: ', lista)
print('A soma dos números da lista é: ', sum(lista))
print('A multiplicação dos resultados é: ', mult)