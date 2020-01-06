#Exercício 14 
#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
print ('Informe 10 numeros')
pares = 0
impares = 0
for i in range(0, 10):
    numero = int(input('Informe um numero: '))
    if (numero % 2 == 0):
        pares = pares + 1
    else:
        impares = impares + 1
print()
print ('A quantidade de números pares são:', pares)
print ('A quantidade de números impares são:', impares)