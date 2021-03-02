# uztaistīt funkciju, kas paņem divus sarakstus kā parametrus, un atrod
# lielāko vērtību no abiem sarakstiem

# saraksti random ģenerēti no 0-20 un ar random garumu - no 5 - 25

import random

def create_list():
    list_length = random.randint(5, 25)
    numbers_list = []
    for i in range(list_length):
        numbers_list.append(random.randint(0, 20))
    return numbers_list

def largest_number(list1, list2):
    
    biggest = list_1[0]
    
    for val in list_1:
        if val > biggest:
            biggest = val
        else:
            continue
    
    for val in list_2:
        if val > biggest:
            biggest = val
        else:
            continue
    
    return biggest


if __name__ == "__main__":
    
    list_1 = create_list()
    print(list_1)
    
    list_2 = create_list()
    print(list_2)
    
    print(largest_number(list_1, list_2))        

