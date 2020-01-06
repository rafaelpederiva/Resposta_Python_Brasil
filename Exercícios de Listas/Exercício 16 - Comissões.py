#Exercício 16 
'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe
 $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em
 uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que 
 determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''
lista_vend = []
salario_base = 200
print('*'*60)
print('\033[32mCálculo de salário - (Para encerrar o programa digite -1)\033[m')
print('*'*60)
j = 1
while True:
    dados = float(input('Digite o valor em vendas do vendedor %d: ' %j))
    if dados == -1:
        break
    else:
        vendas = dados * 0.09
        lista_vend.append(vendas + salario_base)
    j = j + 1
inicio = 200
final = 299
lista_contador = []
for i in range(len(lista_vend)):
    if (lista_vend[i] >= inicio) and (lista_vend[i] <= final):
        lista_contador.append(lista_vend[i])
    else:
        print(inicio,' - ',final,' : ',len(lista_contador))
        lista_contador = []
        inicio = inicio + 100
        final = final + 100