#Exercício 41 
'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, 
quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67'''
divida = float(input('\nDigite o valor da dívida: '))
print('\n>Tabela de Juros\n------------------\nParcelas      Juros\n'
      '01 ------------ 0%\n'
      '03 ------------ 10%\n'
      '06 ------------ 15%\n'
      '09 ------------ 20%\n'
      '12 ------------ 25%\n')
lista_juros = [(1,0),(3,0.10),(6,0.15),(9,0.20),(12,0.25)]
while True:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    if (parcelas == 1) or (parcelas == 3) or (parcelas == 6) or (parcelas == 9) or (parcelas == 12):
        break
    else:
        print('Opção inválida\n')

lista_porc = []
for i in range(5):
    if parcelas == lista_juros[i][0]:
        lista_porc.append(lista_juros[i][1])

valor_juros = divida * lista_porc[0]
divida_total = divida + valor_juros

if parcelas == 1:
    valor_parcelas = divida_total
else:
    valor_parcelas = divida_total / parcelas

print('\nValor da Dívida     Valor Juros     Qtd Parcelas    Valor da Parcela')
print('%15.2f %15.2f %16.0f %19.2f'%(divida_total, valor_juros, parcelas, valor_parcelas))