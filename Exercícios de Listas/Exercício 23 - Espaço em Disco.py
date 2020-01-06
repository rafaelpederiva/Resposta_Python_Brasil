#Exercício 23 
'''A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este 
problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através 
de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado 
"relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do 
programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo 
programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.'''

# ABRINDO E SALVANDO EM UMA LISTA OS DADOS DO ARQUIVO "usuarios.txt"
with open('Exercícios de Listas/usuarios.txt', 'r') as arquivo:       
    lista_dados = arquivo.read().splitlines() 
    # .read() retorna dados do arquivo   
    # .splitlines() retorna uma lista onde cada linha é um elemento dessa lista

# SALVANDO USUÁRIOS E BYTES EM LISTAS
lista_nomes = []
lista_bytes = []
for i in range(len(lista_dados)):
    lista_nomes.append(lista_dados[i][0:15])
    lista_bytes.append(int(lista_dados[i][16:len(lista_dados[i])]))

# FUNÇÃO DE CONVERSÃO DE BYTES PARA MEGABYTES
def byte_para_mega(lista):
    lista_megabyte = []
    for i in range(len(lista)):
        lista_megabyte.append(round(lista[i] / 1048576, 2))
    return lista_megabyte

# FUNÇÃO DE CONVERSÃO DE PORCENTAGEM
def porcentual(lista):
    lista_porcentagem = []
    total = sum(lista)
    for i in range(len(lista)):
        lista_porcentagem.append(round((lista[i] / total) * 100, 2))
    return lista_porcentagem

# SALVANDO OS DADOS CONVERTIDOS NO DOCUMENTO "relatorio.txt"
mega = byte_para_mega(lista_bytes)
porc = porcentual(lista_bytes)
with open ('Exercícios de Listas/relatorio.txt','w') as arquivo:
    arquivo.write('ACME Inc.               Uso do espaco em disco pelos usuarios\n')
    arquivo.write('-'*62)
    arquivo.write('\nNr. Usuario         Espaco utilizado\t% do uso\n\n')
    
    contador = 1
    for f in range(len(lista_nomes)):
        arquivo.write('%-3.2s'%contador + '%16.16s'%lista_nomes[f] + '%14.14s MB'%str(mega[f]) + '%11.11s'%str(porc[f]) + '% \n')
        contador += 1

    soma = sum(mega) 
    media = soma / len(mega)
    arquivo.write('\nEspaco total ocupado: %.7s MB\n' %str(soma))
    arquivo.write('Espaco medio ocupado: %.6s MB' %str(media))
