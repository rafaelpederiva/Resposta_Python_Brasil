#Exercício 19 
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
soma = 0
lista = []
while True:
    num = int(input('Digite o número: '))
    if num == 0:
        break
    elif (num < 0) or (num > 1000):
        print('Dados incorretos!! Os números devem ser de 0 a 1000!')
    else:
        soma = soma + num
        lista.append(num)
print('O menor valor da lista é: ', min(lista))
print('O maior valor da lista é: ', max(lista))
print('A soma dos valores é: ', soma)