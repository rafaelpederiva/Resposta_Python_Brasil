#Exercício 13
# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo
# igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para 
# valores dentro da faixa de forma elegante.

def desenhaMoldura(linha, coluna):
    print('+', end='')
    print('-' * linha, end='')
    print('+')    
    caracter = '|'
    validador = 0
    while coluna > validador:
        print(f'{caracter}{caracter:>{linha + 1}}')
        validador += 1
    print('+', end='')
    print('-' * linha, end='')
    print('+')

l = int(input('Informe o valor da linha: '))
c = int(input('Informe o valor da coluna: '))

if l > 20:
    l = 20
if c > 20:
    c = 20

desenhaMoldura(l, c)
