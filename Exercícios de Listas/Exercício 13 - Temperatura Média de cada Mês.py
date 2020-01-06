#Exercício 13 
'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual 
das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 
1 – Janeiro, 2 – Fevereiro, . . . ).'''
mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
temp = []
for i in range(len(mes)):
    dados = float(input('Digite a temperatuda do mês de %s: ' %mes[i]))
    temp.append(dados)
media = sum(temp) / len(mes)
print('-'*30)
print('A média anual é de: \033[32m %.2f ºC \033[m' % media)
print('-'*30)
print('Os meses que ficaram acima da média são:')
print()
for s in range(len(mes)):
    if temp[s] > media:
        print('%d - %s ' %(s + 1,mes[s]))