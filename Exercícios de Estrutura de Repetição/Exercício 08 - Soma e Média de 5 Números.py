#Exercício 08
#Faça um programa que leia 5 números e informe a soma e a média dos números.
lista = []
for i in range(0,5):
    numero = int(input('Informe o %dº número: ' %(i + 1)))
    lista.append(numero)
media = sum(lista) / len(lista)
print('A soma da lista é %d e a sua média é %d' %(sum(lista), media))