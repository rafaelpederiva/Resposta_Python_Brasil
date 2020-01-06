#Exercício 04
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogal = ['A', 'E', 'I', 'O', 'U']
letra = input('Digite uma letra: ').upper()
validador = False

for i in range(len(vogal)):
    if letra == vogal[i]:
        validador = True

if validador == True:
    print('A letra "%s" é vogal!' %letra)
else:
    print('A letra "%s" é consoante!' %letra)