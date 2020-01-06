#Exercício 16
'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá 
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, 
    sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; '''
import math    

print('Equaçao do 2o grau da forma: ax² + bx + c')    
a = int( input('Coeficiente a: '))
if( a == 0 ):
    print('Não é equação de segundo grau!')
else:
    b = int( input('Coeficiente b: '))
    c = int( input('Coeficiente c: '))
    delta = b * b - (4 * a * c)
    if delta < 0:
        print('Delta menor que 0. Raízes imaginárias!')
    elif delta==0:
        raiz = -b / (2*a)
        print('Delta=0 , raiz = ',raiz)
    else:
        raiz1 = (-b + math.sqrt(delta) ) / ( 2 * a) 
        raiz2 = (-b - math.sqrt(delta) ) / ( 2 * a)
        # MATH.SQRT RETORNA A RAIZ QUADRADA
        print('Raizes: ',raiz1,' e ',raiz2)

