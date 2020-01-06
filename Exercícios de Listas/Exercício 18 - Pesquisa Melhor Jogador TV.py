#Exercício 18 
'''Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua 
equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista
digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação 
foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir 
outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta 
função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor 
calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são 
fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação 
em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0
Resultado da votação:
Foram computados 8 votos.
Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.'''
lista = []
while True:
    dados = int(input('Número do jogador (O=fim): '))
    if dados == 0:
        break
    elif (dados >= 1) and (dados <= 23):
        lista.append(dados)
    elif (dados != 1) and (dados != 23):
        print('Dados incorretos! Para computar os votos, digite somente números de 1 à 23.')
print('Foram computados %d votos' % len(lista))
print('Jogador     Votos      %')
for i in range(0, 23):
    contador = lista.count(i + 1)
    porcentagem = contador / len(lista) * 100
    if contador != 0:
       print('%-2d           %2d       %2.1f' %((i + 1), lista.count(i + 1), porcentagem),'%')
import statistics
melhor_jogador = statistics.mode(lista)
cont_melhor_jogador = lista.count(melhor_jogador)
porc_melhor_jogador = lista.count(melhor_jogador) / len(lista) * 100
print('O melhor jogador foi o número', melhor_jogador, ' com', cont_melhor_jogador, 'votos, correspondendo a',
      porc_melhor_jogador, '% do total dos votos.')