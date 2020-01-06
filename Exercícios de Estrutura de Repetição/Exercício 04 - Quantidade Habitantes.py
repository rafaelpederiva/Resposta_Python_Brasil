#Exercício 04
'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população 
de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
para  que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''
Populacao_A = 80000
Populacao_B = 200000
Ano = 0

while Populacao_A <= Populacao_B:
    Populacao_A += Populacao_A * 0.03
    Populacao_B += Populacao_B * 0.015
    Ano += 1

print ( "A população A ultrapassa ou iguala a população B em %d anos" %Ano )