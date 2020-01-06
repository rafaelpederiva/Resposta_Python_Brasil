#Exercício 27 
'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto 
    de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs 
    adquiridas e escreva o valor a ser pago pelo cliente. '''
lista = [  {'produto': 'MORANGO', 'preço_ate_5kg': 2.50, 'preço_acima_5kg': 2.20},
           {'produto':    'MAÇÃ', 'preço_ate_5kg': 1.80, 'preço_acima_5kg': 1.50}  ]
preço_final = 0
while True:
    produto = input('Digite o produto desejado (Maçã ou Morango): ').upper()
    if (produto == "MAÇÃ") or (produto == "MORANGO"):
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
            
if preço_final > 25.00:
    desconto = preço_final * 0.10
    print('\nO valor a ser pago é de R$ %3.2f '%(preço_final - desconto) )
else:
    print('\nO valor a ser pago é de R$ %3.2f '%preço_final)
