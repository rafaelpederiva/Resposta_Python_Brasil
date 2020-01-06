#Exercício 38 
'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo 
que o usuário digite o salário inicial do funcionário.'''
admissao = int(input('Digite o ano de admissão: '))
ano_atual = int(input('Digite o ano atual: '))
salario = float(input('Digite o salário inicial do funcionário: '))
ajuste = salario * 0.015
salario_ajustado = salario + ajuste
periodo = (ano_atual - admissao) - 1
if periodo == 0:
    print('\nO salário atual é de R$ %.2f' %salario_ajustado)
else:
    for i in range(periodo):
        salario_ajustado *= 1.03
    print('\nO salário atual é de R$ %.2f' %salario_ajustado)