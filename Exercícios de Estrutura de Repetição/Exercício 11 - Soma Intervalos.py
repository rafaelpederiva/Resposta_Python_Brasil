#Exercício 11 
#Altere o programa anterior para mostrar no final a soma dos números.
inicial = int(input('Informe o valor inicial: '))
final = inicial
while (final <= inicial):
    final = int(input('Informe o valor final: '))
    if (final <= inicial):
        print ('O valor final deve ser maior que o valor inicial!')
soma = 0
for i in range(inicial, final + 1):
      print (i)
      soma = soma + i
print('A soma é: ', soma)