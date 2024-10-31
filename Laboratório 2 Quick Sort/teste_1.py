import numpy as np
from quicksort import *

rand_array = np.random.randint(0,800,20) 
print(rand_array)
quick_sort_hoare(rand_array, 0, len(rand_array) - 1)
print(rand_array)
