#Exercício 43 
'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item 
(preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.'''
cardapio = [ {'especificação': 'Cachorro Quente', 'codigo': 100, 'preço': 1.20},
             {'especificação':   'Bauru Simples', 'codigo': 101, 'preço': 1.30},
             {'especificação':   'Bauru com Ovo', 'codigo': 102, 'preço': 1.50},
             {'especificação':      'Hambúrguer', 'codigo': 103, 'preço': 1.20},
             {'especificação':   'Cheeseburguer', 'codigo': 104, 'preço': 1.30},
             {'especificação':    'Refrigerante', 'codigo': 105, 'preço': 1.00} ]

print('Cardápio Lanchonete:\n Especificação   Código  Preço\n' +
      'Cachorro Quente 100     R$ 1,20\n' +
      'Bauru Simples   101     R$ 1,30\n' +
      'Bauru com ovo   102     R$ 1,50\n' +
      'Hambúrguer      103     R$ 1,20\n' +
      'Cheeseburguer   104     R$ 1,30\n' +
      'Refrigerante    105     R$ 1,00\n\n' +
      'Para encerrar digite "0"\n' )
lista = []
while True:
    pedido = int(input('Digite o código do produto: '))
    if (pedido >= 100) and (pedido <= 105):
        lista.append(pedido)
    elif pedido < 0:
        break
    else:
        print('Dados inválidos')

print('\nEspecificação   Qtd   Valor_Unit  Valor_Total')
print('-' * 45)
for i in cardapio:
    if lista.count(i['codigo']) != 0:
        contador = lista.count(i['codigo'])
        print('%-15.15s  %2.0i    R$%6.2f     R$%6.2f' %( i['especificação'], 
                                                      contador, 
                                                      i['preço'], 
                                                      (contador * i['preço'])  ) )
print('-' * 45)
total_compra = 0
for i in cardapio:
    if lista.count(i['codigo']) != 0:
        contador = lista.count(i['codigo'])
        total_compra = total_compra + (contador * i['preço'])
print('Valor a pagar:                      R$%6.2f\n' %total_compra)

# UTILIZANDO APENAS LISTAS 

# print('Cardápio Lanchonete:\n\n' +
#         'Especificação   Código  Preço\n' +
#         'Cachorro Quente 100     R$ 1,20\n' +
#         'Bauru Simples   101     R$ 1,30\n' +
#         'Bauru com ovo   102     R$ 1,50\n' +
#         'Hambúrguer      103     R$ 1,20\n' +
#         'Cheeseburguer   104     R$ 1,30\n' +
#         'Refrigerante    105     R$ 1,00\n\n' +
#         'Para encerrar digite "0"\n'
#         )

# codigo = [100, 101, 102, 103, 104, 105]
# especificacao = ['Cachorro Quente', 'Bauru Simples', 'Bauru com Ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
# preco = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]

# lista_pedidos = []
# contador = 1
# while True:
#     pedido = int(input('Digite o código do %dº produto: '%contador))
#     if pedido == 0:
#         break
#     elif (pedido != 100) and (pedido != 101) and (pedido != 102) and (pedido != 103) and (pedido !=104) and (pedido != 105):
#         print('Código inválido')
#     else:
#         lista_pedidos.append(pedido)
#         contador += 1

# soma_total = 0
# print('\nProduto            Qtd        Preço Unitário        Preço Total')
# print('---------------    ----       -------------         ------------')
# for i in range(len(codigo)):
#     if lista_pedidos.count(codigo[i]) != 0:
#         print(
#               '%-20.20s' %especificacao[i] + 
#               '%-10.2s' %lista_pedidos.count(codigo[i]) +
#               'R$ %8.2f           ' %preco[i] +
#               'R$ %8.2f' %(lista_pedidos.count(codigo[i]) * preco[i])               
#               )
#         soma_total = soma_total + (lista_pedidos.count(codigo[i]) * preco[i])
# print('----------------------------------------------------------------')
# print('Total Geral do Pedido: R$ %5.2f \n' %soma_total)