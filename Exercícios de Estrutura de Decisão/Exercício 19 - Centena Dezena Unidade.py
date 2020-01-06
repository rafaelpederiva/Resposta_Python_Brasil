#Exercício 19 
'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 '''
lista = []
while True:
    num = input('Informe um número menor que 1000: ')
    if int(num) < 1000:
        lista.append(num)
        break
    else:
        print('O número deve ser menor que 1000 para validação!!')
desc = [    {'numero':  0, 'desc_cent': 'centena',  'desc_dez':  'dezena',  'desc_uni': 'unidade' },
            {'numero':  1, 'desc_cent': 'centena',  'desc_dez':  'dezena',  'desc_uni': 'unidade' },
            {'numero':  2, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'},
            {'numero':  3, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'},
            {'numero':  4, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'},
            {'numero':  5, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'},
            {'numero':  6, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'},
            {'numero':  7, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'},
            {'numero':  8, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'},
            {'numero':  9, 'desc_cent': 'centenas', 'desc_dez': 'dezenas',  'desc_uni': 'unidades'} ]

if len(lista[0]) == 3:
    for i in desc:
        if int(lista[0][0]) == i['numero']:
            centena = i['desc_cent']
        if int(lista[0][1]) == i['numero']:
            dezena = i['desc_dez']
        if int(lista[0][2]) == i['numero']:
            unidade = i['desc_uni']
    print('%i %s %i %s %i %s' % (int(lista[0][0]), centena, int(lista[0][1]), dezena, int(lista[0][2]), unidade))

elif len(lista[0]) == 2:
    for i in desc:
        if int(lista[0][0]) == i['numero']:
            dezena = i['desc_dez']
        if int(lista[0][1]) == i['numero']:
            unidade = i['desc_uni']
    print('%i %s %i %s' % (int(lista[0][0]), dezena, int(lista[0][1]), unidade))

elif len(lista[0]) == 1:
    for i in desc:
        if int(lista[0][0]) == i['numero']:
            unidade = i['desc_uni']
    print('%i %s' % (int(lista[0][0]), unidade))

