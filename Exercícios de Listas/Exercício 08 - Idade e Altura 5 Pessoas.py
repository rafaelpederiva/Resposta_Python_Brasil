#Exercício 08 
'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a 
altura na ordem inversa a ordem lida.'''
listaIdade = []
listaAltura = []
for i in range(0,5):
    idade = int(input('Digite a idade da %d pessoa: ' % (i + 1)))
    altura = float(input('Digite o peso da %d pessoa: ' % (i + 1)))
    listaIdade.append(idade)
    listaAltura.append(altura)
print('A idade das pessoas em ordem reversa é: ', listaIdade[::-1])
print('A altura das pessoas em ordem reversa é: ', listaAltura[::-1])