#Exercício 11
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(0,10):
    n1 = int(input('Isira o %dº valor para o vetor 1: ' %(i + 1)))
    n2 = int(input('Isira o %dº valor para o vetor 2: ' %(i + 1)))
    n3 = int(input('Isira o %dº valor para o vetor 2: ' %(i + 1)))
    vetor1.append(n1)
    vetor2.append(n2)
    vetor3.append(n3)
vetor4 = []
for i in range(0,10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
print('O vetor 1 é composto pelos elementos: ', vetor1)
print('O vetor 2 é composto pelos elementos: ',vetor2)
print('O vetor 3 é composto pelos elementos: ',vetor3)
print('O dois vetores intercalados são: ', vetor4)