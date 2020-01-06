#Exercício 13 
'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro 
valor deve aparecer valor inválido.'''
lista = [ {'numero': 1 , 'dia_semana': 'Domingo'},
          {'numero': 2 , 'dia_semana': 'Segunda'},
          {'numero': 3 , 'dia_semana': 'Terça'},
          {'numero': 4 , 'dia_semana': 'Quarta'},
          {'numero': 5 , 'dia_semana': 'Quinta'},
          {'numero': 6 , 'dia_semana': 'Sexta'},
          {'numero': 7 , 'dia_semana': 'Sábado'}  ]
while True:
    numero = int(input('Digite um dia da semana [1-Domingo, 2- Segunda, etc.]: '))
    if (numero >= 1) and (numero <= 7):
        for i in lista:
            if numero == i['numero']:
                print('O número', i['numero'], 'é', i['dia_semana'])
        break
    else:
        print('Dados inválidos!')

