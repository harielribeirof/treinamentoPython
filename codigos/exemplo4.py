# insertion sort
import random

# 
def insertion(lista):
    for i in range(1, len(lista)):
        chave = lista[i]             
        j = i - 1                
        while j >= 0 and lista[j] > chave: 
            lista[j+1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista                        
lista = []
for i in range(50):
    lista.append(random.randint(1,100))
print('ANTES: \n' + str(lista))
lista = insertion(lista)
print('DEPOIS: \n' + str(lista))