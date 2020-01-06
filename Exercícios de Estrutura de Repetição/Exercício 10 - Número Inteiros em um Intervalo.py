#Exercício 10 
#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
inicial = int(input('Informe o valor inicial: '))
final = inicial
while (final <= inicial):
    final = int(input('Informe o valor final: '))
    if (final <= inicial):
        print ('O valor final deve ser maior que o valor inicial!')
for i in range(inicial, final + 1):
      print(i)

