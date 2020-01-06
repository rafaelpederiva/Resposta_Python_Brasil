#Exercício 46 
'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, 
o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa
que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição 
acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos 
são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
-------------------------------
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
-------------------------------
Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m
-------------------------------
Resultado final:
Rodrigo Curvêllo: 5.9 m'''
lista = []
lista2 = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
nome = input('Nome do Atleta: ')
if nome != "":
    for i in range(0,5):
        salto = float(input('%s Salto: ' %(lista2[i])))
        lista.append(salto)
    lista_ordenada = sorted(lista, reverse=True)
    
    melhor_salto = lista_ordenada[0]
    pior_salto = lista_ordenada[4]
    soma = lista_ordenada[1] + lista_ordenada[2] + lista_ordenada[3]
    media = soma / 3

    print('\n\nAtleta: ', nome)
    print('-------------------------------')
    for f in range(0,5):
        print(lista2[f], 'Salto: ', lista_ordenada[f])
    print('-------------------------------')
    print('Melhor Salto: ', melhor_salto)
    print('Pior Salto: ', pior_salto)
    print('Média dos demais Saltos: %2.2f' %media)
    print('-------------------------------')
    print('Resultado final:')
    print(nome,': %2.2f' %media)   
else:
    print('Programa Encerrado')

