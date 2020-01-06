#Exercício 39 
'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua
altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, 
junto com suas alturas.'''
dicionario = {}
lista = []
for i in range(0,10):
    dicionario['aluno'] = int(input('\nDigite o número do %dº aluno(a): ' %(i + 1)))
    dicionario['altura'] = float(input('Digite a altura do %dº aluno(a): ' %(i + 1)))
    lista.append(dicionario.copy())

mais_alto = 0.0; mais_baixo = 3.0
for i in lista:
    if mais_alto < i['altura']:
        mais_alto = i['altura']
    if mais_baixo > i['altura']:
        mais_baixo = i['altura']

print('\n- O aluno mais alto é o de número', end=' ')
for i in lista:
    if i['altura'] == mais_alto:
        print('{} com {} metros. ' .format(i['aluno'], i['altura']))

print('- O aluno mais baixo é o de número', end=' ')
for i in lista:
    if i['altura'] == mais_baixo:
        print('{} com {} metros. ' .format(i['aluno'], i['altura']))
