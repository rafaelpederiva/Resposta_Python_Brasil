#Exercício 08
# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 
def inteiros(numero):
    return len((str(numero)))

n = str(input('Digite um número: ')).strip()

print(f'Esse número tem {inteiros(n)} dígitos')
