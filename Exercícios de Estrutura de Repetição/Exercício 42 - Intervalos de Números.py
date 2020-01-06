#Exercício 42 
'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes 
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''
lista_0_25 = []
lista_26_50 = []
lista_51_75 = []
lista_76_100 = []
while True:
    dados = int(input('Digite um número: '))
    if (dados >= 0) and (dados <= 25):
        lista_0_25.append(dados)
    elif (dados >= 26) and (dados <= 50):
        lista_26_50.append(dados)
    elif (dados >= 51) and (dados <= 75):
        lista_51_75.append(dados)
    elif (dados >= 76) and (dados <= 100):
        lista_76_100.append(dados)
    elif dados > 100:
        print('Número não registrado, não consta em nenhum intervalo!')
    elif dados < 0:
        break
print('Interválo  -- Quantidade'
      '\n[ 0 -  25] -- ',len(lista_0_25),
      '\n[26 -  50] -- ',len(lista_26_50),
      '\n[51 -  75] -- ',len(lista_51_75),
      '\n[76 - 100] -- ',len(lista_76_100),
      )
