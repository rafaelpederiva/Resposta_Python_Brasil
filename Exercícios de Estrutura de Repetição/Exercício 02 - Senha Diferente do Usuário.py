#Exercício 02 
'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma 
mensagem de erro e voltando a pedir as informações.'''
while True:
    usuario = input('Informe um nome de usuario: ')
    senha = input('Informe a senha: ')
    if usuario ==  senha:
        print('A senha não pode ser igual ao nome do usuário')
    else:
        print('Usuário cadastrado')
        break