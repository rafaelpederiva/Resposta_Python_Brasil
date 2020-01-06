#Exercício 20 
'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. '''
lista = []
for i in range(0,3):
    nota = float(input('Digite a %dª nota: ' %(i + 1)))
    lista.append(nota)
media = sum(lista) / len(lista)
if (media >= 7) and (media <= 9.9):
    print('Aprovado')
    print('A média do aluno foi: ', media)
elif media < 7:
    print('Reprovado')
    print('A média do aluno foi: ', media, ' para ser aprovado é necessário no mínimo 7.')
elif media == 10:
    print('Aprovado com Distinção')
    print('O aluno atingiu a nota máxima!')