#Exercício 16 
'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere 
que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 
R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
print()
print('Cálculo de quantidade de latas de tinta a serem compradas')
print()
area = float(input('Digite a quantidade (m²) a serem pintadas: '))
lata = 3 * 18
#Se o número de m² não for múltiplo de 54 (lata) acrecenta uma lata
if area % lata != 0:
  qtd_latas = int(area / lata) + 1
else:
  qtd_latas = area / lata
valor = qtd_latas * 80
print()
print('Você precisará de %d latas(s) a um custo de %.2f' %(qtd_latas, valor))
print()