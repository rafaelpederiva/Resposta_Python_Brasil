#Exercício 14  
'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''
perguntas = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']
respostas = []
print('-'*60)
print('\033[33mPara as pergunta responda "S" para sim e "N" para não. \033[m')
print('-'*60)
for i in range(len(perguntas)):
    dados = input('%s ' %(perguntas[i])).upper()
    respostas.append(dados)
print('-'*60)
if respostas.count('S') == 2:
    print('\033[33mSuspeito \033[m')
elif (respostas.count('S') == 3) or (respostas.count('S') == 4):
    print('\033[33mCumplice \033[m')
elif respostas.count('S') == 5:
    print('\033[31mAssassino \033[m')
else:
    print('\033[34mInocente \033[m')
print('-'*60)