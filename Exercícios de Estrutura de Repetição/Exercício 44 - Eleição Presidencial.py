#Exercício 44 
'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''
print(  'Eleição presidencial\n' +
        '1 - José \n' +
        '2 - João \n' +
        '3 - Pendro \n' + 
        '4 - Lucas \n' +
        '5 - Nulo \n' +
        '6 - Branco\n' +
        '0 - Encerrar\n'    )

candidatos = {  1 : 'José', 
                2 : 'João', 
                3 : 'Pedro',
                4 : 'Lucas',
                5 : 'Nulo',
                6 : 'Branco' }
                
total_votos = []
while True:
    voto = int(input('Informe o seu voto: '))
    if voto == 0:
        break
    elif (voto == 1) or (voto == 2) or (voto == 3) or (voto == 4) or (voto == 5) or (voto == 6):
        total_votos.append(voto)
    else:
        print('Valor Inválido!')

soma_total = 0
codigo = 1
total_branco = 0
total_nulo = 0
print('\nCandidato   Total Votos')
print('---------   -----------')
for i in range(len(candidatos)):    
    soma_total = soma_total + total_votos.count(codigo)       
    # SE OS VOTOS FOREM "NULOS"
    if codigo == 5: 
        total_nulo = total_nulo + total_votos.count(codigo) 
        codigo += 1        
    # SE OS VOTOS FOREM "BRANCO"
    elif codigo == 6:
        total_branco = total_branco + total_votos.count(codigo) 
        codigo += 1      
    # VOTOS PARA OS CANDIDATOS  
    else: 
        print(  
            '%-13.13s'  %candidatos[codigo] + 
            '%-10.10s' %total_votos.count(codigo) 
            )
        codigo += 1

print('\nForam Computados' , soma_total, 'votos.')
print('Votos Nulos foram:', total_nulo, 'votos. Correspondendo a %2.2f' %((total_nulo / soma_total) * 100) + ' % do total dos votos.')
print('Votos Brancos foram:', total_branco, 'votos. Correspondendo a %2.2f' %((total_branco / soma_total) * 100) + ' % do total dos votos.\n')