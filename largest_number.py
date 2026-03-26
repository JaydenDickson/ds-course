def largest_rec(list_int):
    if len(list_int) == 1:
        return list_int[0]
    elif largest_rec(list_int[0:len(list_int)-1]) < list_int[len(list_int)-1]:
        return list_int[len(list_int)-1]
    else:
        return largest_rec(list_int[0:len(list_int)-1])


list_int = [1,8,3,2,3,4]
print(largest_rec(list_int))