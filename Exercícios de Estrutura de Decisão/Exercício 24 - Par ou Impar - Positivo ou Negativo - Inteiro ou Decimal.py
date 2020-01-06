#Exercício 24 
'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação 
deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.'''
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print('\nEscolha qual operação deseja realizar:\n1 - para Adição\n2 - para Subtração\n3 - para Multiplicação\n4 - para Divisão\n')
while True:
    operacao = int(input("Digite o número da operação: "))
    if (operacao == 1) or (operacao == 2) or (operacao == 3) or (operacao == 4):
        break
    else:
        print('Dados invárilos!\nPara prosseguir digite [1]-Adição, [2]-Subtração, [3]-Multiplicação ou [4]-Divisão.')

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
else:
    resultado = num1 / num2

print('\n\nO resultado da operação é: ', resultado, end='\nEsse número é: ')
if resultado % 2 == 0:
    print('par,', end=' ')
else:
    print('impar,', end=' ')
if resultado >= 0:
    print('positivo', end=' e ')
else:
    print('negativo', end=' e ')
if resultado == round(resultado):
    print('inteiro.\n')
else:
    print('decimal.\n')
