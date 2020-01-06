#Exercício 04 
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
lista = []
for i in range(0,4):
    nota = float(input('Digite a nota do %dº bimestre: '%(i + 1)))
    lista.append(nota)
media = sum(lista) / len(lista)
print('A média do aluno foi: ',media)