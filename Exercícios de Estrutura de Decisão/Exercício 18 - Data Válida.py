#Exercício 18
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input("digite uma data com o seguinte formato dd/mm/aaaa: ")
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
                print('Data válida!')
            else:
                print('Data inválida! (Erro: DIA)')  
        else:
            print('Data inválida! (Erro: MES)')    

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
                print('Data válida!')
            else:
                print('Data inválida! (Erro: DIA)')  
        else:
            print('Data inválida! (Erro: MES)')                   
else:
    print('Data inválida! A data não pode conter números zeros ou negativos!')

