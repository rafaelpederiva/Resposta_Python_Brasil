#Exercício 16 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja 
maior que 500.'''
primeiro = 0
print(primeiro)
segundo = 1
while (segundo < 700):
    print(segundo)
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro