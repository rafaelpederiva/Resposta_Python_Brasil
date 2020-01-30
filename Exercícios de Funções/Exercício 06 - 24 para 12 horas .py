#Exercício 06
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 
# em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um 
# parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores 
# de entrada todas as vezes que desejar. 
import time
import os

def hora_ampm(horas, minutos):
    if horas <= 12:
        nova_hora = horas
        sigla = 'AM'
    else:
        nova_hora = horas - 12
        sigla = 'PM'
    return str(nova_hora) + ':' + str(minutos) + ' ' + sigla    

def limpa_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    print('\nInforme primeiro a hora e em seguida os minutos.\n0 para sair\n')
    h = int(input('Informe a hora: '))
    if (h > 23) or (h < 0):
        print('Hora inválida!')
        time.sleep(2)
        limpa_tela()
    elif h == 0:
        print('\nPrograma encerrado!\n')
        break
    else:
        m = int(input('Informe os minutos: '))
        if (m < 0) or (m > 60):
            print('Minutos inválidos!')
            time.sleep(2)
            limpa_tela()
        else:
            limpa_tela()
            print(hora_ampm(h,m))
