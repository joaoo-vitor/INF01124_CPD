from hashing import *
import pandas as pd
import datetime


table_sizes= [3793, 6637, 9473, 12323, 15149]

hash_table = {}
df_players = pd.read_csv('arquivos-suporte/players.csv')
df_searches = pd.read_csv('arquivos-suporte/consultas.csv')

# Para cada tamanho de tabela
for table_size in table_sizes:
    # Cria tabela vazia
    hash_table = start_hash_table(table_size)

    # Conta tempo
    start = datetime.datetime.now()
    # Insere cada jogador na lista da posição adequada 
    for index, row in df_players.iterrows():
        key = int(row['sofifa_id'])
        insert_hash_table(key, row.to_dict(), hash_table, table_size)
    end = datetime.datetime.now()
    table_creation_time = (end-start).microseconds/1000

    # Registra estatísticas
    occupancy_rate = 0
    maximum_list_size = 0
    list_size_avg = 0
    for i in table_size:
        list_size=len(hash_table[i])
        if list_size>0:
            occupancy_rate +=1
            list_size_avg+=list_size
            if(list_size>maximum_list_size):
                maximum_list_size=list_size
    # A média de tamanho das listas é calculado para apenas listas não vazias (cujo numero é o occupancy rate nesse momento)
    list_size_avg/=occupancy_rate
    occupancy_rate/=table_size
            
    # Faz consultas para cada valor do csv de consultas
    # Registra estatísticas
    start = datetime.datetime.now()
    # Dicionario que hospeda se encontrou o jogador e quantos testes foram feitos
    dict_found_tests = []
    for index, row in df_searches.iterrows():
        key = row[0]
        tests_qty, player = search_hash_table(key, 'sofifa_id', hash_table, table_size)
        if(player):
            dict_found_tests.append({'id':key, 'name':player['name'], 'tests_qty':tests_qty})
        else:
            dict_found_tests.append({'id':99999, 'name':'NAO_ENCONTRADO', 'tests_qty':tests_qty})

    end = datetime.datetime.now()
    searches_time = (end-start).microseconds/1000
