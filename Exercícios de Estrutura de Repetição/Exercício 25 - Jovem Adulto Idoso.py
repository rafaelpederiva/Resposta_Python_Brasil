#Exercício 25 
'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre
0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''
lista_jovem = []
lista_adulto = []
lista_idoso = []
print('Digitar as idades, para encerrar o programa digite 0.')
while True:
    num = int(input('Digite a idade: '))
    if num == 0:
        break
    elif num < 0:
        print('A idade não pode ser menor que zero!!!')
    elif (num > 0) and (num <= 25):
        lista_jovem.append(num)
    elif (num >= 26) and (num <= 60):
        lista_adulto.append(num)
    else:
        lista_idoso.append(num)
media_jovem = sum(lista_jovem) / len(lista_jovem)
media_adulto = sum(lista_adulto) / len(lista_adulto)
media_idoso = sum(lista_idoso) / len(lista_idoso)

print('A média de idade das pessoas jovens é: ', media_jovem)
print('A média de idade das pessoas adultas é: ', media_adulto)
print('A média de idade das pessoas idosas é: ', media_idoso)