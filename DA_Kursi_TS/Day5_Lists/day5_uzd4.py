#%% my version

def uzd4(list_arg):
    x = 0
    for i in range(len(list_arg)):
        if x < list_arg[i]:
            x = list_arg[i]
        else:
            continue
    
    return x

if __name__ == "__main__":
    my_list = [1,6,3,4,-1,3,4,7]
    print(uzd4(my_list))
    
#%% other version

def biggest_number(number_list):
    biggest = number_list[0] # vajag likt number_list[0], jo ja nu ir tikai negatīvi skaitļi listā
                                # tad iedos 0
    for val in number_list:
    
        if val > biggest:
            biggest = val
    
    return biggest

if __name__ == "__main__":
    my_list = [1,6,3,4,-1,3,4,7]
    print(biggest_number(my_list))