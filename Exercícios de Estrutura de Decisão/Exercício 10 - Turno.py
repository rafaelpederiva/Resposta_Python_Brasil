#Exercício 10 
'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
turno = [   {'sigla':'M', 'descrição': 'Matutino', 'mensagem': 'Bom dia!'},
            {'sigla':'V', 'descrição': 'Vespetino', 'mensagem': 'Boa Tarde!'},
            {'sigla':'N', 'descrição': 'Noturno', 'mensagem': 'Boa Noite'}     ]
while True:
    t = input('Informe o seu turno [M]-Matutino [V]-Vespetino [N]-Noturno: ').upper()
    if (t == 'M') or (t == 'V') or (t == 'N'):
        for i in turno:
            if t == i['sigla']:
                print('Você estuda no período %s. %s' %(i['descrição'], i['mensagem']))
        break
    else:
        print('Turno Inválido! Digite [M]-Matutino [V]-Vespetino [N]-Noturno!')
