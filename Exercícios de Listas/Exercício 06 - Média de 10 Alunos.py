#Exercício 06 
'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número 
de alunos com média maior ou igual a 7.0.'''
notas = []
for i in range(0, 10):
    notasAluno = []
    for j in range(0, 4):
        notasAluno.append(float(input('Informe a nota do aluno %.d: ' % (i + 1))))
    notas.append(notasAluno)
alunosMedia = 0
for notasAluno in notas:
    somaNotas = 0
    for nota in notasAluno:
        somaNotas = somaNotas + nota
    if ((somaNotas / 4.0) >= 7.0):
        alunosMedia += 1
print ('%d alunos ficaram acima da media' % alunosMedia)