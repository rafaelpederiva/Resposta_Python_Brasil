#Exercício 18
#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
condition = True
soma = 0
lista = []
print('Informe uma sequência de números')
print('Para descobrir a soma e o maior e menor entre eles')
print('Digite o número zero para encerrar a sequência.')
print()
while condition:
    num = int(input('Digite o número: '))
    if num != 0:
        soma = soma + num
        lista.append(num)
    else:
        break      
print('O menor valor da lista é: ', min(lista))
print('O maior valor da lista é: ', max(lista))
print('A soma dos valores é: ', soma)