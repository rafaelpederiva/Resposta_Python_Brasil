# Exercício 07
# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa
# deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago 
# na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor
# igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade 
# e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, 
# cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso. 
import time
import os

dicionario = {}

def limpa_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def valorPagamento(valor, prestações, vencimento):
    lista = []
    for i in range(prestações):
        valor_dividido = valor / prestações
        limpa_tela()
        print('Informe o dia de pagamento da prestação {}, dia de vencimento: {}' .format((i+1), vencimento))
        # print('Informe o dia de pagamento da prestação %i, dia de vencimento: %i' %(i + 1), vencimento) )
        dia_pagamento = int(input('\n>> '))
        if dia_pagamento > vencimento:
            valor_dividido = valor_dividido * 1.03
            qtd_dias = dia_pagamento - vencimento
            for f in range(qtd_dias):
                valor_dividido = valor_dividido * 1.001
            print('Pagamento com juros e multa: R$ %6.2f' %valor_dividido)
            dicionario['parcela'] = i + 1
            dicionario['dia_pgt'] = dia_pagamento
            dicionario['v_programado'] = valor / prestações
            dicionario['v_pago'] = valor_dividido
            lista.append(dicionario.copy())
            time.sleep(2)
        else:
            print('Pagamento: R$ %6.2f' %valor_dividido)
            dicionario['parcela'] = i + 1
            dicionario['dia_pgt'] = dia_pagamento
            dicionario['v_programado'] = valor / prestações
            dicionario['v_pago'] = valor_dividido
            lista.append(dicionario.copy())
            time.sleep(2)
    limpa_tela()
    print('Relatório de pagamento')
    print('\nParcela    Dia de Pagamento   Valor Programado   Valor Pago')
    print('-' * 60)
    valor_total = 0
    for i in lista:
        print('%-11i %-18i R$%-17.2f R$%-8.2f' %( i['parcela'], i['dia_pgt'], i['v_programado'], i['v_pago']))
        valor_total = valor_total + i['v_pago']
    print('-' * 60)
    print('Valor total pago:                               R$%10.2f' %valor_total)
    input('\n\nAperte enter para reiniciar o programa ')
    
while True:
    limpa_tela()
    print('Informe o valor da parcela ou "0" para encerrar o programa')
    val = float(input('\n>> '))
    if val == 0:
        limpa_tela()
        print('Programa encerrado\n')
        break
    else:
        limpa_tela()
        print('Informe o total de prestações')
        prt = int(input('\n>> '))
        limpa_tela()
        print('Informe o dia de vencimento')
        vct = int(input('\n>> '))
        limpa_tela()
        valorPagamento(val, prt, vct)

