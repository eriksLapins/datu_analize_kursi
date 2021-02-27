#%% my version
import random

def list_creating():
    
    list1 = []
    list2 = []
    
    for i in range(3):
        list1.append(random.randint(0, 3))
        list2.append(random.randint(0, 3))
    
    return list1, list2
    
def list_comparison(list1, list2):
    
    x = 0
    
    
    for val in list1:
        if val in list2:
            if list2.count(val) == list1.count(val):
                x += 1
    
    y = 0            
    for val in list2:
        if val in list1:
            if list1.count(val) == list2.count(val):
                y += 1
            
    if x == y and x == len(list1) and y == len(list2):
        return True
    else:
        return False

if __name__ == "__main__":
    list1, list2 = list_creating()

    print(list1)
    print(list2)
    
    print(list_comparison(list1, list2))
    
#%% other version

def compare_lists(a, b):
    if len(a) != len(b):
        return False
    else:
        if a.sort() == b.sort():
            return True
        else:
            return False
        
if __name__ == "__main__":
    int_list = [1, 3, 2, 4]
    int_list_2 = [4, 1, 2, 3]
    print(compare_lists(int_list, int_list_2))
    
#%% other version

def compare_lists2(a, b):
    if len(a) != len(b):
        return False
    
    a.sort()
    b.sort()
    
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True
        
if __name__ == "__main__":
    int_list = [1, 3, 2, 4]
    int_list_2 = [4, 1, 2, 3]
    print(compare_lists2(int_list, int_list_2))
    
#%% more python version

def compare_lists3(a, b):
    if len(a) != len(b):
        return False
    
    a.sort()
    b.sort()
    
    if set(a) != set(b):
        return False
    
    return True
        
if __name__ == "__main__":
    int_list = [1, 3, 2, 4]
    int_list_2 = [4, 1, 2, 3]
    print(compare_lists3(int_list, int_list_2))
    
