#Exercício 03 
#Faça um Programa que peça dois números e imprima a soma.
lista = []
for i in range(0,2):
    n = int(input('Digite o %dº número: ' %(i + 1)))
    lista.append(n)
print('A soma do número {} e {} é {}.' .format(lista[0], lista[1], sum(lista)))