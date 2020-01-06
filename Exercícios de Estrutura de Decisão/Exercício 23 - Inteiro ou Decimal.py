#Exercício 23
#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
num = float(input('Numero original: '))
if num == round(num):
    print("Inteiro")
else:
    print("Decimal")