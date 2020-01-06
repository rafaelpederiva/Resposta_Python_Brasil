#Exercício 17 
'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere 
que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.
   * Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
   * comprar apenas latas de 18 litros;
   * comprar apenas galões de 3,6 litros;
   * misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga 
	 e sempre arredonde os valores para cima, isto é, considere latas cheias. '''
qtd = float(input('Digite a quantidade (m²) a serem pintados: '))

lata = 6 * 18
galao = 6 * 3.6
area = qtd * 1.1

# CÁLCULO COM APENAS LATAS
if area % lata != 0:
  qtd_latas = int(area / lata) + 1
else:
  qtd_latas = area / lata
valor_lata = qtd_latas * 80

# CÁLCULO COM APENAS GALÕES
if area % galao != 0:
  qtd_galao = int(area / galao) + 1
else:
  qtd_galao = area / galao
valor_galao = qtd_galao * 25

# CÁLCULO COM LATAS E GALÕES (MELHOR PREÇO)
metros = area
mix_latas = metros // lata
metros -= mix_latas * lata
if metros <= 64.2:
    mix_galao = metros // galao
    valor_mixgalao = mix_galao * 25
    if metros < 21.6:
        mix_galao += 1
        valor_mixgalao = mix_galao * 25
else:
    mix_latas += 1
    mix_galao = 0
    valor_mixgalao = 0
valor_mixlata = mix_latas * 80
mix_total = valor_mixgalao + valor_mixlata
folga = area * 0.1

print('\nPara pintar a área de %d m² com %d m² de folga será preciso:' %(qtd,folga))
print('\nLatas:\n%d lata(as), ao custo de R$%s,00 ' %(qtd_latas,valor_lata))
print('\nGalões:\n%d galão(ões), ao custo de R$%s,00 ' %(qtd_galao,valor_galao))
print('\nLatas e Galões (melhor preço):\n%d lata(s) e %d galão(ões) ao custo de R$%s,00\n'
      %(mix_latas,mix_galao,int(mix_total)))