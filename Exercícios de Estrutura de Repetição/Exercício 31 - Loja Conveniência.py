#Exercício 31 
'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa 
que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das 
mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra 
e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa 
deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...'''
import os
print('Para encerrar a compra digite 0.')
lista = []
contador = 1
while True:
    produto = float(input('Digite o valor %dº produto: ' %contador))
    if produto == 0:
        dinheiro = float(input('Digite o valor em dinheiro: '))
        soma = sum(lista)
        troco = dinheiro - soma

        cont_lista = 0
        print('\nRecibo')
        print('-' *25)
        for i in lista:
            print('Produto %d:     R$ %7.2f ' %(cont_lista + 1, lista[cont_lista]))
            cont_lista += 1
        print('-' *25)
        print('Total:         R$ %7.2f ' %soma)
        print('Dinheiro:      R$ %7.2f ' %dinheiro)
        print('Troco:         R$ %7.2f ' %troco)
        lista = []
        contador = 1
        continuar = input('\n\nPara continuar digite ENTER ')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        continue
    else:
        lista.append(produto)
        contador += 1