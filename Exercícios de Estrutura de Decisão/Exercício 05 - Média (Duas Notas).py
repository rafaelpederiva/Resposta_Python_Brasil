#Exercício 05
'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por 
aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. '''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media == 10:
    print('A média do aluno foi %2.f' %media)    
    print('"Aprovado com Distinção"')
elif media >= 7 and media < 10:
    print('A média do aluno foi %2.f' %media)
    print('"Aprovado"')
elif media < 7:
    print('A média do aluno foi %2.f' %media)
    print('"Reprovado"')
