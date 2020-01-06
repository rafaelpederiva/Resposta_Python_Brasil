#Exercício 45 
'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a 
resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto 
por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos
usarem o programa.'''
import time
import os
# gabarito = ['A','B','C','D','E','E','D','C','B','A']

# LANÇAMENTO DE NOTAS PROFESSOR
print('Acesso administrativo.\nLançamento de notas\n')
gabarito = []
for f in range(10):
    lancamento = input('Alternativa Questão %d: ' %(f + 1))
    gabarito.append(lancamento)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# LANÇAMENTO DE NOTAS ALUNOS
notas = dict()
lista = list()
lista_soma = list()
contador = 1
while True:
    notas.clear() # LIMPANDO O DICIONÁRIO    
    if os.name == 'nt': # LIMPANDO O TERMINAL
        os.system('cls')
    else:
        os.system('clear')    
    soma = 0 # LIMPANDO A VARIÁVEL SOMA    
    aluno = input('\nNome do %sº aluno ou "0" para sair: ' %contador)
    notas['aluno'] = aluno
    print()
    if aluno == '0': # PARAR O PROGRAMA AO DIGITAR ZERO
        break
    else:        
        for i in range(10):
            questao = input('Digite a resposta da questão número %d: '%(i + 1))
            if questao == gabarito[i]: # SE A QUESTÃO FOR IGUAL DO GABARITO 
                soma = soma + 1 # SOMAR 
        lista_soma.append(soma)
        print('\nRegistrando dados, aguarde...') 
        time.sleep(3)  # AGUARDANDO 3 SEGUNDOS
        print('\nDados registrados com sucesso!')     
        time.sleep(1) # AGUARDANDO 1 SEGUNDO
        contador += 1 # SOMANDO MAIS UM NÚMERO NA VARIÁVEL CONTADOR
    notas['acertos'] = soma # ADICIONAR O ALUNO E A SOMA DAS RESPOSTAS CORRETAS NO DICIONÁRIO
    lista.append(notas.copy()) # FAZER UMA CÓPIA DO DICIONÁRIO DENTRO DA LISTA

if os.name == 'nt': # LIMPANDO O TERMINAL
    os.system('cls')
else:
    os.system('clear')  
# IMPRIMINDO RESULTADOS NA TELA
print('Lista de acertos por aluno')
print('-' *30)
print('Aluno     Acertos')
print('-----     --------')
for b in lista:
    print('%-10.10s'%(b['aluno']) + ' %2.2d'%(b['acertos']))
print('\nO maior quantidade de acerto obtido foi: %d' %max(lista_soma) + ' e a menor quantidade de acertos obtidos foi: %d' %min(lista_soma))
print('A quantidade de alunos que utlizaram o sistema foi: ', len(lista_soma))
print('A média da turma foi de: %2.2f \n\n' %(sum(lista_soma) / len(lista_soma)))

