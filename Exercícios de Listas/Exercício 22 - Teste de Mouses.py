#Exercício 22 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas
encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um 
deles, para verificar o que se pode aproveitar deles. Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa
deverá receber um número indeterminado de entradas, cada uma contendo:
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; 
a.necessita troca do cabo ou conector; 
a.quebrado ou inutilizado 
Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100
Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%'''
print('\nAnálise de defeitos de Mouses\n')
print('Digite: \n1 = Para troca de esfera\n2 = Para limpeza digite \n3 = Para troca do conector digite'
    '\n4 = Quebrado ou inutilizado digite\n0 = Para sair\n')
lista = []
defeitos = [
            'necessita da esfera',
            'necessita de limpeza',
            'necessita troca do cabo ou conector',
            'quebrado ou inutilizado'
            ]
contador = 1
while True:
    dados = int(input('Digite o Código de defeito do %dº Mouse: '%contador))
    if dados == 0:
        break
    elif (dados < 0) or (dados > 4):
        print('\033[31mDados incorretos!! Digite números de 1 a 4. \033[m')
    else:
        lista.append(dados)
        contador += 1
print('\nQuantidade de mouses analisados: ',len(lista))
print('Situação                                   Quantidade    Percentual')
for i in range(0, 4):
    contador = lista.count(i + 1)
    porcentagem = contador / len(lista) * 100
    print('%-2d %-35s       %2d           %4.1f' %(
        (i + 1),
        defeitos[i],
        lista.count(i + 1),
        porcentagem),
        '%')