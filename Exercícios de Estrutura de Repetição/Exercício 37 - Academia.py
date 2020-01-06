#Exercício 37 
'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da
digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados
os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''
import os

dicionario = dict()
lista = list()
print('Para encerrar digite zero!')
while True:
    codigo = int(input('Código: '))
    if codigo == 0:
        break
    else:
        dicionario['codigo'] = codigo
        dicionario['altura'] = float(input('Altura do cliente de código %d: ' %codigo))
        dicionario['peso'] = float(input('Peso do cliente de código %d: ' %codigo))  
        lista.append(dicionario.copy())      
        input('\nAperte ENTER para continuar...')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('Para encerrar digite zero!')

maior_altura = 0; menor_altura = 2.0; maior_peso = 0; menor_peso = 300
for i in lista:
    if maior_altura < i['altura']:
        maior_altura = i['altura']
    if menor_altura > i['altura']:
        menor_altura = i['altura']    
    if maior_peso < i['peso']:
        maior_peso = i['peso']
    if menor_peso > i['peso']:
        menor_peso = i['peso']
print('Relatório')
print('-'*30 )
print('Mais alto:')
for i in lista:
    if maior_altura == i['altura']:
        print('código {} ------> {} metros.' .format( i['codigo'], i['altura']))  
print('-'*30 )
print('Mais baixo:') 
for i in lista: 
    if menor_altura == i['altura']:
        print('código {} ------> {} metros.' .format( i['codigo'], i['altura']))  
print('-'*30 )
print('Mais Gordo:') 
for i in lista:  
    if maior_peso == i['peso']:
        print('código {} ------> {} quilos.' .format(i['codigo'], i['peso']))
print('-'*30 )
print('Mais Magro:')
for i in lista:
    if menor_peso == i['peso']:
        print('código {} ------> {} quilos.' .format(i['codigo'], i['peso']))
print()

# OUTRA FORMA DE FAZER ( COM 3 LISTAS )

# lista_codigo = []
# lista_altura = []
# lista_peso = []
# while True:
#     codigo = int(input('\nCódigo: '))
#     if codigo != 0:
#         altura = float(input('Altura do cliente de código %d: '%codigo))
#         peso = float(input('Peso do cliente de código %d: '%codigo))

#         lista_codigo.append(codigo)
#         lista_altura.append(altura)
#         lista_peso.append(peso)

#         continue
#     else:
#         break        
# #DESCOBRIR OS MAIORES E MENORES VALORES DAS LISTAS        
# maior_altura = max(lista_altura)
# menor_altura = min(lista_altura)
# maior_peso = max(lista_peso)
# menor_peso = min(lista_peso)
# #DESCOBRIR A POSIÇÃO QUE SE ENCONTRA OS MAIORES E MENORES VALORES
# posicao_maior_altura = lista_altura.index(maior_altura)
# posicao_menor_altura = lista_altura.index(menor_altura)
# posicao_maior_peso = lista_peso.index(maior_peso)
# posicao_menor_peso = lista_peso.index(menor_peso)
# print('\nO cliente mais alto é o de código ',lista_codigo[posicao_maior_altura], 'com ',maior_altura)
# print('O cliente mais baixo é o de código',lista_codigo[posicao_menor_altura], 'com ',menor_altura)
# print('O cliente mais magro é o de código',lista_codigo[posicao_menor_peso], 'com ',menor_peso)
# print('O cliente mais gordo é o de código',lista_codigo[posicao_maior_peso], 'com ',maior_peso)