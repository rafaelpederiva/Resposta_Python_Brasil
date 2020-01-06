#Exercício 40 
'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes 
dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''
dicionario = {}
lista = []
for i in range(0,5):
    dicionario['cidade'] = int(input('\nDigite o código da %dª cidade: ' %(i + 1)))
    dicionario['veiculos'] = int(input('Digite o nº de veículos de passeio da %dª cidade: ' %(i + 1)))
    dicionario['acidentes'] = int(input('Digite o nº de acidentes da %dª cidade: '%(i + 1)))
    dicionario['indice'] = int( (dicionario['acidentes'] * 100) / dicionario['veiculos'] )
    lista.append(dicionario.copy()) 

maior_indice = 0; menor_indice = 100000
for i in lista:
    if maior_indice < i['indice']:
        maior_indice = i['indice']
    if menor_indice > i['indice']:
        menor_indice = i['indice']

print('\n- O maior índice de acidente é da cidade', end=' ')
for i in lista:
    if maior_indice == i['indice']:
        print('{} com {} %.' .format(i['cidade'], i['indice']))

print('- O menor índice de acidente é da cidade', end=' ')
for i in lista:
    if menor_indice == i['indice']:
        print('{} com {} %.' .format(i['cidade'], i['indice']))

soma = 0
for i in lista:
    soma = soma + i['veiculos']
media = soma / len(lista)
print('- A média de veículos das {} cidades é de {} veículos.' .format(len(lista), int(media)))

soma = 0; qtd = 0
for i in lista:
    if i['veiculos'] < 2000:
        soma = soma + i['acidentes']
        qtd = qtd + 1
if soma == 0:
    print('- Não exitem cidades com menos de 2000 veículos\n')
else:
    media = soma / qtd
    print('- A média de acidentes das cidades com menos de 2000 veículos é de {} acidentes.\n' .format(int(media)))

