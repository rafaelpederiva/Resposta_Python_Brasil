#Exercício 11
'''Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de 
mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. '''

lista = [ {'numero_mes':  1, 'mes_extenso':  'Janeiro'},{'numero_mes':  2, 'mes_extenso': 'Fevereiro'},
          {'numero_mes':  3, 'mes_extenso':    'Março'},{'numero_mes':  4, 'mes_extenso':     'Abril'},
          {'numero_mes':  5, 'mes_extenso':     'Maio'},{'numero_mes':  6, 'mes_extenso':     'Junho'},
          {'numero_mes':  7, 'mes_extenso':    'Julho'},{'numero_mes':  8, 'mes_extenso':    'Agosto'},
          {'numero_mes':  9, 'mes_extenso': 'Setembro'},{'numero_mes': 10, 'mes_extenso':   'Outubro'},
          {'numero_mes': 11, 'mes_extenso': 'Novembro'},{'numero_mes': 12, 'mes_extenso':  'Dezembro'} ]

def mesPorExtenso(nMes):
    for i in lista:
        if nMes == i['numero_mes']:
            return i['mes_extenso']

data = input("\nDigite uma data com o seguinte formato dd/mm/aaaa: ")

# VALIDANDO DATA
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])
validador_dia = False
if (dia > 0) and (mes > 0) and (ano > 0):    
    # *********** ANO BISSEXTO ***********
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        mes_dia = [ {'mes':  1, 'ultimo_dia': 31}, {'mes':  2, 'ultimo_dia': 29}, {'mes':  3, 'ultimo_dia': 31},
                    {'mes':  4, 'ultimo_dia': 30}, {'mes':  5, 'ultimo_dia': 31}, {'mes':  6, 'ultimo_dia': 30},
                    {'mes':  7, 'ultimo_dia': 31}, {'mes':  8, 'ultimo_dia': 31}, {'mes':  9, 'ultimo_dia': 30},
                    {'mes': 10, 'ultimo_dia': 31}, {'mes': 11, 'ultimo_dia': 30}, {'mes': 12, 'ultimo_dia': 31}  ]

        if (mes >= 1) and (mes <= 12):
            for i in mes_dia:
                if mes == i['mes']:
                    if dia <= i['ultimo_dia']:
                        validador_dia = True
            if validador_dia == True:
                extenso = mesPorExtenso(mes)
                print('\n{} de {}\n' .format(extenso, ano))
            else:
                print('\nNULL\nData inválida! (Erro: DIA)\n')  
        else:
            print('\nNULL\nData inválida! (Erro: MES)\n') 
    # *********** ANO NÃO BISSEXTO ***********
    else:
        mes_dia = [ {'mes':  1, 'ultimo_dia': 31}, {'mes':  2, 'ultimo_dia': 28}, {'mes':  3, 'ultimo_dia': 31},
                    {'mes':  4, 'ultimo_dia': 30}, {'mes':  5, 'ultimo_dia': 31}, {'mes':  6, 'ultimo_dia': 30},
                    {'mes':  7, 'ultimo_dia': 31}, {'mes':  8, 'ultimo_dia': 31}, {'mes':  9, 'ultimo_dia': 30},
                    {'mes': 10, 'ultimo_dia': 31}, {'mes': 11, 'ultimo_dia': 30}, {'mes': 12, 'ultimo_dia': 31}  ]

        if (mes >= 1) and (mes <= 12):
            for i in mes_dia:
                if mes == i['mes']:
                    if dia <= i['ultimo_dia']:
                        validador_dia = True
            if validador_dia == True:
                extenso = mesPorExtenso(mes)
                print('\n{} de {}\n' .format(extenso, ano)) 
            else:
                print('\nNULL\nData inválida! (Erro: DIA)\n')  
        else:
            print('\nNULL\nData inválida! (Erro: MES)\n')                   
else:
    print('\nNULL\nData inválida! A data não pode conter números zeros ou negativos!\n')
