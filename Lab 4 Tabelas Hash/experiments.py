from hashing import *
import pandas as pd
import datetime


table_sizes= [3793, 6637, 9473, 12323, 15149]

hash_table = {}
df_players = pd.read_csv('arquivos-suporte/players.csv')
df_searches = pd.read_csv('arquivos-suporte/consultas.csv')

# Dicionário para ter estatísticas (cada chave é um tamanho de tabela, o valor é um dicionario de estatisticas)
dict_statistics= {}

# Dicionario que hospeda se encontrou o jogador e quantos testes foram feitos (chave é o valor da consulta)
dict_found_tests = {}

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
    for i in range(table_size):
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

    for index, row in df_searches.iterrows():
        key = row[0]
        tests_qty, player = search_hash_table(key, 'sofifa_id', hash_table, table_size)
        if not(key in dict_found_tests):
            dict_found_tests[key] = {}
        if(player):
            dict_found_tests[key]['id']=key
            dict_found_tests[key]['name']=player['name']
            dict_found_tests[key]['tests_qty'+str(table_size)]=tests_qty

        else:
            dict_found_tests[key]['id']=99999
            dict_found_tests[key]['name']='NAO_ENCONTRADO'
            dict_found_tests[key]['tests_qty'+str(table_size)]=tests_qty

    end = datetime.datetime.now()
    searches_time = (end-start).microseconds/1000

    # Cria nova chave no dicionario para tamanho de tabela atual no dicionario de estatisticas
    dict_statistics[table_size] = {"table_creation_time": table_creation_time, "occupancy_rate":occupancy_rate, "maximum_list_size": maximum_list_size, "list_size_avg": list_size_avg, "searches_time": searches_time}

with open('estatisticas_construção.txt', 'w') as s:
    for info in ['table_creation_time', 'occupancy_rate', 'maximum_list_size', 'list_size_avg']:
        line = ''
        for table_size in table_sizes:
            line += str(dict_statistics[table_size][info]) + ','
        # Remove ultima virgula antes de escrever no arquivo
        s.write(line.rstrip(',') + '\n')

with open('estatisticas_consultas.txt', 'w') as s:
    line = ''
    for table_size in table_sizes:
        line += str(dict_statistics[table_size]['searches_time']) + ','
    # Remove ultima virgula antes de escrever no arquivo
    s.write(line.rstrip(',') + '\n')
    for key in dict_found_tests:
        line = ''
        line += str(dict_found_tests[key]['id']) + ','+ str(dict_found_tests[key]['name']) + ','
        for table_size in table_sizes:
            line += str(dict_found_tests[key]['tests_qty'+str(table_size)]) + ','
        # Remove ultima virgula antes de escrever no arquivo
        s.write(line.rstrip(',') + '\n')
