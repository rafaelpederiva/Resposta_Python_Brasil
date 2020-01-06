#Exercício 05 
'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e
permita repetir a operação.'''
Populacao_A = int(input('Informe a população A: '))
Crescimento_A = float(input('Informe a taxa de crescimento da população A: '))
Populacao_B = int(input('Informe a população B: '))
Crescimento_B = float(input('Informe a taxa de crescimento da população B: '))
Ano = 0 

Calc_Taxa_A = Crescimento_A / 100
Calc_Taxa_B = Crescimento_B / 100

while Populacao_A <= Populacao_B:
    Populacao_A += Populacao_A * Calc_Taxa_A
    Populacao_B += Populacao_B * Calc_Taxa_B
    Ano += 1

print ( "A população A ultrapassa ou iguala a população B em %d anos" %Ano )