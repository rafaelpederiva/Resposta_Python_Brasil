#Exercício 19
'''Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa 
deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos
para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido 
completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800
O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.'''
print('-'*50)
print('\033[32mPesquisa: Melhores Sistemas Operacionais!\033[m')
print('-'*50)
print('\033[32mDigite: \033[34m1)Windows Server    2)Unix        3)Linux')
print('        4)Netware           5)Mac OS      6)Outro\033[m')
print('-'*50)
print('Para terminar a pesquisa digite zero "0"\n')

Lista_SO = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro','']
lista = []
while True:
    dados = int(input('Digite o número do Sistema operacional (que na sua opinião) é o melhor: '))
    if dados == 0:
        break
    elif (dados >= 1) and (dados <= 6):
        lista.append(dados)
    elif (dados != 1) and (dados != 6):
        print('\033[31mDados incorretos! Para computar os votos digite apenas números de 1 a 6.\033[m')

print('\nSistema Operacional     Votos     %')
print('-------------------     -----   ----')
for i in range(0,6):
    Sist_Op = Lista_SO[i]
    contador = lista.count(i + 1)
    porcentagem = lista.count(i + 1)/len(lista) * 100
    print('%-14.14s %13.0f %6.0f'%(Sist_Op,contador,porcentagem),'%')
print('-------------------     -----')
print('Total de Votos: %12.3s\n' %(len(lista)))

import statistics
melhor_SO = statistics.mode(lista)
cont_melhor_SO = lista.count(melhor_SO)
porc_melhor_SO = lista.count(melhor_SO) / len(lista) * 100
for n in range(len(Lista_SO)):
    if n == melhor_SO:
        print('O Sistema Operacional mais votado foi o %s, com %.0f votos,'
                ' correspondendo a %.0f ' % (
            Lista_SO[n-1],
            cont_melhor_SO,
            porc_melhor_SO),
            '% dos votos. \n\n')