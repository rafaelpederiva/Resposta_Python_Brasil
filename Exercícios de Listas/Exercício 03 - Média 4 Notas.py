#Exercício 03
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for i in range(0, 4):
    notas.append(float(input('Informe uma nota: ')))
soma = 0.0
print ('\nNotas Digitadas:')
for i in range(0, 4):
    print ('Nota %d: %.2f' % (i + 1, notas[i]))
    soma = soma + notas[i]
print ('A Média das notas: %.2f' % (soma / 4.0))