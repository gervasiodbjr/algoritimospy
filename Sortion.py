import random

# TEST ARRAYS
simple = [4, 7,  2, 5, 4, 0]
any_numbers = random.sample(range(1, 1000), 42)
already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 
                    32, 34, 39, 40, 42, 76, 87, 99, 112]
inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]
repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]



#######################
#     BUBBLE SORT     #
#######################
def bubblesort(arr):
    n = len(arr)
    for j in range(1, n):
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                tmp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = tmp

# bubblesort(inversed)
# print(inversed)


#######################
#    SELECTION SORT   #
#######################
# ind = 1
# m1 -> 0 _to_ (ind)
# m2 -> ind _to_ len(arr)
# ie, ii
# ie -> ind _to_ len(arr)
# ii -> 0 _to_ (ind);
def selectionsort(arr):
    n = len(arr)
    for ie in range(1, n):
        for ii in range(0, ie):
            if arr[ie] < arr[ii]:
                tmp = arr[ii]
                arr[ii] = arr[ie]
                arr[ie] = tmp

# selectionsort(any_numbers)
# print(any_numbers)


#######################
#    SELECTION SORT   #
#######################
# ie -> 0 _to_ (len(arr) -1)
# buscar o menor valor em 'arr' e identificar a posicao 'pos'
# trocar posicao arr[ie] <-> arr[pos]
def selectionsort(arr):
    n = len(arr)
    for ie in range(0, n - 1):
        for ii in range(ie, n):
            if arr[ii] < arr[ie]:
                tmp = arr[ie]
                arr[ie] = arr[ii]
                arr[ii] = tmp
    
selectionsort(simple)
print(simple)


#######################
#      MERGE SORT     #
#######################
def mergesort(lista, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (inicio + fim) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1
            
def prn(lista, inicio, meio, fim):
    print('INICIO: ' + str(inicio) + ' | MEIO: ' + str(meio) + ' | FIM: ' + str(fim))

# mergesort(inversed)
# print(inversed)


