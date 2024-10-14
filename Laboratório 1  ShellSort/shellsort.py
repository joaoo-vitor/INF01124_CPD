import numpy as np

shell_sequence = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
knuth_sequence = [1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524, 88573, 265720, 797161, 2391484]
ciura_sequence = [1, 4, 10, 23, 57, 132, 301, 701, 1577, 3548, 7983, 17961, 40412, 90927, 204585, 460316, 1035711]

def shell_sort(arr, n, seq_type, should_print):
    # descresce começando no index np até 0 na sequencia dada
    if(seq_type == 'SHELL'):
        seq = shell_sequence
    elif(seq_type == 'KNUTH'):
        seq = knuth_sequence
    elif(seq_type == 'CIURA'):
        seq = ciura_sequence

    # escolhe qual elemento da sequencia comaçar, partindo do ultimo e indo para a esquerda
    index_sequence = len(seq)-1
    while(seq[index_sequence] > n):
        index_sequence -= 1

    if(should_print): 
        print(*arr, f'SEQ={seq_type}') 
    for i in range(index_sequence, -1, -1):
        h = seq[i]
        for j in range(0, h):
            insDiretaShellSort(arr, n, h, j)
        if(should_print): 
            print(*arr, f'INCR={h}') 


def insDiretaShellSort(arr, n, h, f):
    # começa do segundo elemento do segmento até o ultimo
    for j in range(h+f, n, h):
        chave = arr[j]
        i = j-h 
        # insere a nova chave no lugar correto
        while((i>=0) and (arr[i]>chave)):
            arr[i+h] = arr[i]
            i = i-h
        arr[i+h] = chave



