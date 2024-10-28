import numpy as np

def quick_sort_lomuto(arr, i, f):
    if(f>i):
        # partition into two parts
        p = partition_lomuto(arr, i, f)
        # make recursion for both parts 
        quick_sort_lomuto(arr, i, p-1)
        quick_sort_lomuto(arr, p+1, f)

def quick_sort_hoare(arr, i, f):
    if(f>i):
        # partition into two parts
        p = partition_hoare(arr, i, f)
        # make recursion for both parts 
        quick_sort_hoare(arr, i, p-1)
        quick_sort_hoare(arr, p+1, f)
        

def partition_lomuto(arr, left, right):
    chave = arr[left]
    storeIndex = left+1 # index of smaller element
    for i in range(left, right):
        # if the element is smaller than or equal to the pivot
        if(arr[i] < chave):
            #swap values
            swap(arr, i, storeIndex)
            storeIndex+=1
    swap(arr, left, storeIndex-1)
    return storeIndex-1


def partition_hoare(arr, left, right):
    chave = arr[left]
    i=left
    j=right+1
    while(i<j):
        while(arr[i+1]<=chave):
            i+1
            if(i==right):
                break
        while(arr[j-1]<=chave):
            j-=1
            if(j==left):
                break
        swap(arr, i, j)
    swap(arr, left, j)
    return j
    
def swap(arr, a, b):
    tmp = arr[a]
    arr[a]=arr[b]
    arr[b] = tmp


array = np.random.randint(0, 800, size=10)
print(array)
quick_sort_hoare(array, 0, len(array)-1)
print(array)
