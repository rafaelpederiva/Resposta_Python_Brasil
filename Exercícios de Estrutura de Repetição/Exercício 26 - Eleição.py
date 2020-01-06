#Exercício 26 
'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final 
mostrar o número de votos de cada candidato.'''
candidato1 = []
candidato2 = []
candidato3 = []
print('---------------------------')
print('Candidato 1 -------- vote 1')
print('Candidato 2 -------- vote 2')
print('Candidato 3 -------- vote 3')
print('---------------------------')
num = int(input('Digite o número de eleitores: '))
for i in range(1,num+1):
    voto = int(input('Eleitor %d digite seu voto: '%i))
    if voto == 1:
        candidato1.append(voto)
    elif voto == 2:
        candidato2.append(voto)
    elif voto == 3:
        candidato3.append(voto)
print('Candidato 1 recebeu: ',len(candidato1))
print('Candidato 2 recebeu: ',len(candidato2))
print('Candidato 3 recebeu: ',len(candidato3))