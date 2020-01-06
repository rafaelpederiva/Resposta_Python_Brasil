#Exercício 24
'''Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas 
vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos
dos dados.'''
import random

lista = []
for i in range(0, 100):
    lancamento = random.randint(1, 6)
    lista.append(lancamento)

vetor = [1,2,3,4,5,6]
numero = 1
for f in range(len(vetor)):
    cont = lista.count(f + 1)
    print('O número', numero, 'se repetiu ', cont, ' vezes.')
    numero += 1
