import numpy as np

shell_sequence = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
knuth_sequence = [1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524, 88573, 265720, 797161, 2391484]
ciura_sequence = [1, 4, 10, 23, 57, 132, 301, 701, 1577, 3548, 7983, 17961, 40412, 90927, 204585, 460316, 1035711]

def shell_sort(arr, seq_type):
    # descresce começando no index np até 0 na sequencia dada
    if(seq_type == 'SHELL'):
        seq = shell_sequence
    elif(seq_type == 'KNUTH'):
        seq = knuth_sequence
    elif(seq_type == 'CIURA'):
        seq = ciura_sequence
    index_sequence = len(seq)-1
    while(seq[index_sequence] > len(arr)):
        index_sequence -= 1
    print('index encontrado: ', index_sequence)

    print(*arr, f'SEQ={seq_type}') 
    for i in range(index_sequence, -1, -1):
        h = seq[i]
        for j in range(0, h):
            insDiretaShellSort(arr, h, j)
        print(*arr, f'INCR={h}') 


def insDiretaShellSort(arr, h, f):
    n = len(arr)
    for j in range(h+f, n, h):
        chave = arr[j]
        i = j-h 
        while((i>=0) and (arr[i]>chave)):
            arr[i+h] = arr[i]
            i = i-h
        arr[i+h] = chave


array = np.random.randint(0, 100000, size=10)
shell_sort(array, 'SHELL')




# with open('entrada1.txt', 'r') as f:
#     for line in f:
#         arr = line.split()
#         shell_sort(arr, )
