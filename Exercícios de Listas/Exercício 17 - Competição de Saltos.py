#Exercício 17 
'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos
cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa 
deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m'''
for i in range(0,1):
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        print('-'*30)
        print('Programa encerrado!')
    else:
        n = 1
        lista = []
        for f in range(0,5):
            salto = float(input('Digite o %dº salto: ' %n))
            lista.append(salto)
            n = n + 1
if nome == '':
    print('-'*30)
else:
    media = sum(lista) / len(lista)
    print('-'*30)
    print('Atleta: \033[32m',nome,'\033[m')
    print('Saltos: \033[32m',lista[0],' - ',lista[1],' - ',lista[2],' - ',lista[3],' - ',lista[4],'\033[m')
    print('Média dos saltos: \033[32m',media,' m\033[m')
    print('-'*30)