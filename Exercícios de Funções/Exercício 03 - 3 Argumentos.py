#Exercício 03
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 
def soma(n = []):
    for i in range(3):
        numero = int(input('Digite o %iº número: ' %(i + 1)))
        n.append(numero)
    print('\nA soma dos três argumentos é: ', sum(n), '\n')
soma()
