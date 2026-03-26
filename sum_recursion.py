def sum_list(list_int, index_int):
    if index_int == 0:
        return list_int[0]
    else:        
        return sum_list(list_int, index_int-1) + list_int[index_int]


list_int = [1, 2, 3, 4, 5]
index_int = 2
print(sum_list(list_int, index_int))



