#Exercício 24 
#Faça um programa que calcule o mostre a média aritmética de N notas.
lista = []
print('Encontrar média aritmética, para encerrar digite 0.')
while True:
    num = int(input('Digite a nota: '))
    if num == 0:
        break
    else:
        lista.append(num)
media = sum(lista) / len(lista)
print('Á média aritmética é ', media)