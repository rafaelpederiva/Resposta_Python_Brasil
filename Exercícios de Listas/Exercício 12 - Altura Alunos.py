#Exercício 12 
'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem 
altura inferior à média de altura desses alunos.'''
idade = [14,13,13,14,13,13,14,15,10,10,14,13,13,14,13,13,14,15,10,10,14,13,13,14,13,13,14,15,10,10]
altura = [1.80,1.80,1.80,1.80,1.80,1.80,1.80,1.60,1.50,1.50,1.80,1.80,1.80,1.80,1.80,1.80,1.80,1.60,1.50,1.50,1.80,1.80,
        1.80,1.80,1.80,1.80,1.80,1.60,1.50,1.50]
i = 0
soma = 0
while i < len(altura):
    soma = soma + altura[i]
    i = i + 1
media = soma / len(altura)
f = 0
qtd = 0
while f < len(idade):
    if(idade[f] >= 13 and altura[f] < media):
        qtd += 1
    f += 1
print('-'*96)
print('\033[32mA quantidade de alunos com a idade de 13 anos ou mais, que possuem a idade abaixo da media é:\033[31m ',qtd)
print('\033[m-'*96)