#Exercício 47 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica
sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto 
e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser 
conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
---------------------------
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04'''
lista = []
nome = input('Nome do Atleta: ')
if nome != "":
    for i in range(0,7):
        nota = float(input('Nota: '))
        lista.append(nota)
    lista_ordenada = sorted(lista, reverse=True)

    melhor_nota = lista_ordenada[0]
    pior_nota = lista_ordenada[6]
    soma = lista_ordenada[1] + lista_ordenada[2] + lista_ordenada[3] + lista_ordenada[4] + lista_ordenada[5]
    media = soma / 5
    print('\n---------------------------')
    print('Resultado final:')
    print('Atleta: ', nome)
    print('Melhor nota: ', melhor_nota)
    print('Pior Notas: ', pior_nota)
    print('Média: %2.2f' %media)
else:
    print('Programa encerrado!')