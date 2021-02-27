#%% Lists intro

def list_sample(): # define a new method
    my_list = [1,2,3,4,5] # saraksts ar atsevišķiem mainīgajiem
        # var principā būt dažādas vērtības, bet labi būtu ja tas saturētu tikai viena tipa vērtības
    print(str(my_list[0]) + "\n\n")  # var atsaukties uz katru elementu listā ar indexu, kas sākas no 0
    
    
    for x in my_list:
        print(str(x) + "\n")
        
        
    for i in range(len(my_list)): # len(my_list) - norāda lista garumu
        print(my_list[i])
    
    for i in range(0, len(my_list), 2): # printēt katru otro
        print(my_list[i])
    
    print(my_list.count(1)) # saskaitīt kopējo skaitu ar konkrētu elementu listā
        
    # print(my_list[2])
    # print(my_list[-2])
    # print(my_list[:3]) 
    # print(my_list[2:4]) 
    # print(my_list[3:])
    # print(my_list[::2]) # izvada katru otro
    # print(my_list[::-1]) # pretējā virzienā
    
def list_append(): # lieto, kad nezina kas var būt pilnajā listā
    my_list = []
    
    for i in range(5): # gribu ielikt 4 vērtības
        my_list.append(i)

    for x in my_list:
        print(str(x) + "\n")


if __name__ == '__main__':
    list_append()

#%% list as argument

def arg_sample(a):
    for x in a:
        print(x)
    a.append(111) # var veikt izmaiņas, listā, ja tas ir padots kā arguments
    
if __name__ == "__main__":
    
    
    my_list = [1,2,3,4,5]
    my_list2 = [1,2,3,4,6]
    divi_listi = [my_list, my_list2]
    print(divi_listi[1]) # vajag izturēties pret katru datasetu, kā pret individuālu elementu    
    
    
    
    arg_sample(my_list)
    print(my_list)

#%% list as argument 2

def arg_sample(a):
    for x in a:
        print(x)
    a.append(111) # var veikt izmaiņas, listā, ja tas ir padots kā arguments

if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    arg_sample(my_list)
    print(my_list)
    
#%%

def set_sample():
    dic1 = {4: 'geeks', 1: 'for', 3: 'geeks'}
    lst = [4,1,3]
    print(dic1)
    print(lst)
    
    if set(dic1) == set(lst): # set() vienādo sarakstus
        print(dic1)
        print(lst)

if __name__ == "__main__":
    set_sample()