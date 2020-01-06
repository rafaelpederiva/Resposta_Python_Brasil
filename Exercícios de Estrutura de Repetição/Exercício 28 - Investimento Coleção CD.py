#Exercício 28 
'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''
cd = []
num = int(input('Informe a quantidade de CDs: '))
for i in range(1, num + 1):
    valor_cd = float(input('Digite o valor do CD %d: '%i))
    cd.append(valor_cd)
media = sum(cd) / len(cd)
print('A quantidade investida na coleção de CD é de R$ %2.2f' %sum(cd))
print('A média de valores gastas em CDs é de R$ %2.2f ' %media)