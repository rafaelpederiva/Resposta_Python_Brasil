#Exercício 15 
#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
termo = 0
while (termo <= 0):
    termo = int(input('Voce quer a serie de Fibonacci ate qual termo: '))
    if (termo <= 0):
        print('O termo deve ser positivo!')
primeiro = 0
segundo = 1
for i in range(1, termo + 1):
    print(segundo)
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro