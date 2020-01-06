#Exercício 21 
'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas 
de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 
600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro
               notas de 10, uma nota de 5 e quatro notas de 1. '''
while True:
    valor = int(input('Informe quanto deseja sacar: '))
    if valor < 10:
        print('Valor mínimo para saque R$ 10,00.')
        continue
    elif valor > 600:
        print('Valor máximo para saque R$ 600,00')
        continue
    else:
        break
notas = [100, 50, 10, 5, 1]
qtds = []
total = valor
for i in notas:
    qtd = valor // i
    valor -= i * qtd
    qtds.append(qtd)
    
template = 'R$ {:>3}: {:>3} notas'
print('- Valor do saque: R$ ' + str(total) + ',00')
print(template.format('100', qtds[0]))
print(template.format('50', qtds[1]))
print(template.format('10', qtds[2]))
print(template.format('5', qtds[3]))
print(template.format('1', qtds[4]))