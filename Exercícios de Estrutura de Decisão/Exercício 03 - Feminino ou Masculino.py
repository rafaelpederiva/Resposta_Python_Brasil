#Exercício 03
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
gereno = [ {'sigla':'F', 'descrição': 'Feminino'},{'sigla':'M', 'descrição': 'Masculino'} ]
while True:
    sexo = input('Informe o seu gênero [M]-Masculino [F]-Feminino: ').upper()
    if (sexo == 'M') or (sexo == 'F'):
        for i in gereno:
            if sexo == i['sigla']:
                print( i['sigla'], ' - ', i['descrição'] )
        break
    else:
        print('Sexo Inválido! Digite [M]-Masculino ou [F]-Feminino.')
