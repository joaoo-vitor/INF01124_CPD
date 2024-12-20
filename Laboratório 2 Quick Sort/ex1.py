from quicksort import *
import numpy as np
import datetime

results = []

# Abre o arquivo de entrada
with open('entrada-quicksort.txt', 'r') as e:
    print('tamanho,escolha-particionador,particionamento,trocas,recursoes,tempo')
    for line in e:
        arr = line.split()
        arr = list(map(int, arr))
        n = arr.pop(0)  # Remove o primeiro elemento (tamanho do vetor)

        result_line = []

        for particionador in ['aleatorio', 'mediana3']:
            
            # Define o particionador
            if particionador == 'aleatorio':                    
                pivot = np.random.randint(0, len(arr) - 1)
            elif particionador == 'mediana3':
                inicio = arr[0]
                fim = len(arr) - 1
                pivot = (inicio + fim) // 2

            # Ordena array com QuickSort Lomuto
            arr_copy = arr.copy()  
            time_before = datetime.datetime.now()
            arr_copy, trocas, recursoes = quick_sort_lomuto(arr_copy, pivot, len(arr_copy) - 1)
            time_after = datetime.datetime.now()
            milisseconds = (time_after-time_before).microseconds/1000
            result_line = f'{n},{particionador},lomuto,{trocas},{recursoes},{milisseconds:.3f}'   
            results.append(result_line)
            print(result_line)
            
            # Ordena array com QuickSort Hoare
            arr_copy = arr.copy() 
            time_before = datetime.datetime.now()
            trocas, recursoes = quick_sort_hoare(arr_copy, pivot, len(arr_copy) - 1)
            time_after = datetime.datetime.now()
            milisseconds = (time_after-time_before).microseconds/1000
            result_line = f'{n},{particionador},hoare,{trocas},{recursoes},{milisseconds:.3f}'
            results.append(result_line)
            print(result_line)

# Salva no arquivo de saida 
with open('saida-quicksort.txt', 'w') as s:
    for line in results:
        s.write(line + '\n')
