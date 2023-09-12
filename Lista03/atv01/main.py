import numpy as np

data =np.array([
    [29, 79,  9],
    [52, 16, 13],
    [59, 77, 39],
    [28, 23, 94],
    [29, 68, 87],
    [65, 32, 14],
    [62, 54, 95],
    [ 5, 78, 20],
    [23, 38, 29],
    [45, 71, 19],
    [46, 45, 66],
    [18, 26, 59],
    [22, 88, 17],
    [74, 15,  4],
    [73, 87, 36]
])



print(data)



vetor1 = data[:,0]
print(vetor1)

def min(vetor):
    menor =vetor[0]
    for i in range(len(vetor)):
        if(vetor[i]<menor):
            menor =vetor[i]
    return menor

def max(vetor):
    maior =vetor[0]
    for i in range(len(vetor)):
        if(vetor[i]>maior):
            maior =vetor[i]
    return maior

print(min(vetor1))
print(max(vetor1))

# matrizNova=[[0 for j in range(3)] for i in range(15)] 

# for i in range(len(vetor1)):
#     calculoMinMax = ((vetor1[i]-min(vetor1))
#                 /(max(vetor1) -min(vetor1)))
#     matrizNova[i][0]=calculoMinMax
#     print(calculoMinMax)
# print(matrizNova)


   

def minmax(vetor):
    vetoraux1 =vetor[:,0]
    vetoraux2 =vetor[:,1]
    vetoraux3 =vetor[:,2]
    matrizNova=[[0 for j in range(3)] 
    for i in range(15)] 

    for i in range(len(vetoraux1)):   
        calculoMinMax = ((vetoraux1[i]-min(vetoraux1))/(max(vetoraux1) -min(vetoraux1)))
        matrizNova[i][0]=round(calculoMinMax,8)
    for i in range(len(vetoraux2)): 
        calculoMinMax = ((vetoraux2[i]-min(vetoraux2))/(max(vetoraux2) -min(vetoraux2)))
        matrizNova[i][1]=round(calculoMinMax,8)
    for i in range(len(vetoraux3)): 
        calculoMinMax = ((vetoraux3[i]-min(vetoraux3))/(max(vetoraux3) -min(vetoraux3)))
        matrizNova[i][2]=round(calculoMinMax,8)
    return matrizNova

matriz = minmax(data)
print(matriz[0][0])
print(minmax(data))
