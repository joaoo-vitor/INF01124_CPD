
from hashing import *
import pandas as pd

M = 100
hash_table = {}

# Abre o arquivo de entrada
df = pd.read_csv('arquivos-suporte/players.csv')

hash_table = start_hash_table(M)

for index, row in df.iterrows():
    key = int(row['sofifa_id'])
    insert_hash_table(key, row, hash_table, M)

print(search_hash_table(222492, 'sofifa_id', hash_table, M))
