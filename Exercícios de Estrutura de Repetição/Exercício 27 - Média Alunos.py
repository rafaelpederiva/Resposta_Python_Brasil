#Exercício 27 
'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para 
cada turma. As turmas não podem ter mais de 40 alunos.'''
turmas = []
num = int(input('Digite o número de turmas: '))
for i in range(1, num + 1):
    alunos = int(input('Digite a quantidade de alunos da turma %d: ' %i))
    if alunos > 40:
        print('Número máximo de alunos não pode passar de 40!')
        alunos_novo = int(input('Digite denovo essa turma: '))
        turmas.append(alunos_novo)
    else:
        turmas.append(alunos)

for c in range(len(turmas)):
    print('A %dª turma tem %d alunos' %(c+1,turmas[c]))