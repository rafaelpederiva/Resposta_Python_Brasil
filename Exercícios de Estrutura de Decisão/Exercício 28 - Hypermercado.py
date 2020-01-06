#Exercício 28 
'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
    há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
    desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário 
    e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
    valor do desconto e valor a pagar. '''
lista = [  {'produto': 'FILE DUPLO', 'preço_ate_5kg': 4.90, 'preço_acima_5kg': 5.80},
           {'produto':    'ALCATRA', 'preço_ate_5kg': 5.90, 'preço_acima_5kg': 6.80}, 
           {'produto':    'PICANHA', 'preço_ate_5kg': 6.90, 'preço_acima_5kg': 7.80}  ]
           
while True:
    produto = input('Digite o produto desejado (File Duplo, Alcatra e Picanha): ').upper()
    pagamento = input('Cartão Tabajara? [S - Sim] [N - Não]: ').upper()
    if (produto == "FILE DUPLO") or (produto == "ALCATRA") or (produto == 'PICANHA') and (pagamento == 'S') or (pagamento == 'N'):
        quantidade = float(input('\nQuantos quilos vc deseja comprar de %s: ' %produto.lower() ))
        break
    else:
        print('Dados inválidos!')

if quantidade > 5.00:
    for i in lista:
        if produto == i['produto']:
            preço_final = quantidade * i['preço_acima_5kg']
else:
    for i in lista:
        if produto == i['produto']:
            preço_final = quantidade * i['preço_ate_5kg']
            
if pagamento == 'S':
    desconto = preço_final * 0.05
    print('\nO valor a ser pago é de R$ %3.2f '%(preço_final - desconto) )
else:
    print('\nO valor a ser pago é de R$ %3.2f '%preço_final)