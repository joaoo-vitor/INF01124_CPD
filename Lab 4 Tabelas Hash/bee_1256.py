def hash(key, M):
    return key % M


def start_hash_table(M):
    hash_table = {}
    for i in range(M):
        hash_table[i] = []
    return hash_table


def insert_hash_table(key, item, hash_table, M):
    pos = hash(key, M)
    hash_table[pos].append(item)

test_cases = int(input())
answer =''
for i in range(test_cases):
    table_size, number_of_cases = list(map(int, input().split()))

    hash_table = start_hash_table(table_size)
    input_user = input().split()
    for j in range(number_of_cases):
        key = int(input_user[j])
        insert_hash_table(key, key, hash_table, table_size)

    # Print output for the current hash table
    for j in range(table_size):
        line = str(j)+' -> '
        for value in hash_table[j]:
            line+= str(value) + ' -> '
        line+='\\'
        answer+=line+'\n'
    # If is not the last output, print break line
    if(not(i==test_cases-1)):
        answer+='\n'
print(answer, end='')
