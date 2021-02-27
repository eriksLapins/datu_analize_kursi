#%% my version
import random

def uzd3():
    
    random_list = []
    for i in range(5):
        random_list.append(random.randint(0,10))
    
    random_list_reverse = []
    for i in range(4,-1,-1):
            random_list_reverse.append(random_list[i]) 
    
    return random_list, random_list_reverse


if __name__ == "__main__":
    print(uzd3())
    
#%% other version

def task3():
    a = []
    b = []
    
    for i in range(5):
        a.append(random.randint(0,10))
    
    # for i in range(0, len(a)):
    #     b.append(a[len(a)-1-i])
    
    # for i in range(4, -1, -1):
    #     b.append(a[i])
    
    for i in reversed(range(5)):
        b.append(a[i])
        
    print(a)
    print(b)
    
if __name__ == "__main__":
    task3()
        