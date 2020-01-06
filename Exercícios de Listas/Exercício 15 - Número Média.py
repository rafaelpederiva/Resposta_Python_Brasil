#Exercício 15 
'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando 
for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''
notas = []
print('='*33)
print('\033[33mPara sair do programa digite "-1"\033[m')
print('='*33)

while True:
    dados = int(input('Insira uma nota: '))
    if dados == -1:
        break
    else:
        notas.append(dados)
print('A quantidade de valores lidos foram: \033[33m', len(notas),'\033[m')
print('Os valores em sua ordem são: \033[33m', notas,'\033[m')
print('Os valores na ordem inversa (um abaixo do outro) são:')
notas.reverse()

for i in range(len(notas)):
    print('\033[33m',notas[i],'\033[m')
print('A soma dos valores é: \033[33m', sum(notas),'\033[m')
media = sum(notas) / len(notas)
print('A média dos valores é: \033[33m %.2f \033[m' %media)
notas.sort()

listamedia = []
for s in range(len(notas)):
    if notas[s] > media:
        listamedia.append(notas[s])
print('Os valores acima da média são: \033[33m', listamedia, '\033[m')

listasete = []
for f in range(len(notas)):
    if notas[f] < 7:
        listasete.append(notas[f])
print('A quantidade de valores abaixo de sete são: \033[33m', len(listasete),'\033[m', 'Sendo eles: \033[33m',listasete,'\033[m')
print('='*33)
print('\033[33mPrograma encerrado!!!!\033[m')
print('='*33)