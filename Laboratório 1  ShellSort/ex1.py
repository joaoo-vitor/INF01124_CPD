from shellsort import *

with open('Laboratório 1  ShellSort/entrada1.txt', 'r') as f:
    for line in f:
        arr = line.split()
        arr = list(map(lambda x: int(x), arr))
        n = arr.pop(0)
        for sequence in ['SHELL', 'KNUTH', 'CIURA']:
            shell_sort(arr, n, sequence, True)



  

