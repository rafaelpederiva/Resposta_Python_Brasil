#Exercício 33 
'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''
lista = []
contador = 1
while True:
    temp = float(input('Digite a %dª temperatura: ' %contador))
    if temp == 0:
        break
    else:
        lista.append(temp)
        contador += 1
print('A maior temperatura registrada foi: ',max(lista))
print('A menor temperatura registrada foi: ',min(lista))
media = sum(lista) / len(lista)
print('A média foi de: ', media)