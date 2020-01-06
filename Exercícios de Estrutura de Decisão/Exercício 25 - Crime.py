#Exercício 25
'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
    positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
    Caso contrário, ele será classificado como "Inocente". '''
print('Digite "S" para sim e "N" para não\n')
lista = [  'Telefonou para a vítima? ',
           'Esteve no local do crime? ',
           'Mora perto da vítima? ',
           'Devia para vítima? ',
           'Já trabalhou com a vítima? ' ]
respostas = []
contador = 0
for i in lista:
    print(lista[contador],end=' ')
    inf = input().upper()
    if (inf == 'S') or (inf == 'N'):
        respostas.append(inf)
        contador += 1
    else:
        print('Dados incorretos!')
        print('Fim do programa!\n')
        break
if len(respostas) == 5:
    res_final = respostas.count('S')
    if res_final == 2:
        print('Suspeito\n')
    elif (res_final == 3) or (res_final == 4):
        print('Cúmplice\n')
    elif res_final == 5:
        print('Assassino\n')
    else:
        print('Inocente\n')
