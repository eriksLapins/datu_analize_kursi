#%% dict start

def dict_sample():
    sample = {
        'studentName': 'Test1',
        'studentLastName': 'Test2',
        'course': 3
        }
    
    for val in sample.values():
        print(val)
    
    for val in sample.keys():
        print(val)

    for key, val in sample.items():
        print(str(key) + ": " + str(val)) # if we have an integer, in this case, we need to specify it as a string

    list_of_dict = [
        {
        'studentName': 'Test1',
        'studentLastName': 'Test2',
        'course': 3            
        },
        {
        'studentName': 'Test1',
        'studentLastName': 'Test2',
        'course': 3       
        }
        ]
    
    print(list_of_dict)
    
if __name__ == '__main__':
    dict_sample()
    
#%% file handling
import day7_uzd1 as stParse

def task1():
    name = input("Lūdzu ievadiet studenta vārdu!")
    last_name = input("Lūdzu ievadiet studenta uzvārdu")
    course = int(input("Lūdzu ievadiet studenta kursu"))
 
    student_dict = stParse.create_student_dict(name, last_name, course)

    for key, val in student_dict.items(): # .items() is used to look for keys AND values, we ask for what we want
                                            # .values() - get values
                                            # .keys() - get keys
        print(key + ": " + str(val))


if __name__ == '__main__':
    f = open('test.txt', 'w') # w - pārrakstīt, write; a - papildināt, add
    f.write("Musu pirmais fails\n") # write pārraksta visu uz šīm vērtībām
    f.write("jauna rinda\n")
    f.close()
    
    f = open('test.txt', 'r')
    # var izprintēt saturu ar:
    # print(f.read())
    # var iziet cauri failam ar:
    for position, line in enumerate(f):
        if position == 0: # pirmo rindu
            a = line.rstrip("\n") # lai noņemtu enter pēc rindas
            print(a)
    print("aaa")
# =============================================================================
#     # var arī ar range'us izmantot, lai izprintētu vairākas rindas
#     in_range = [0, 1]
# 
#     for position, line in enumerate(f):
#         if position in in_range: # pirmo rindu
#             print(line)
# =============================================================================
# =============================================================================
#     # varam izprintēt līnijas    
#     lines_list = f.readlines()
#     print(lines_list)
# =============================================================================
# =============================================================================
#     # varam ierakstīt līnijas (ja ir funkcija 'write' ieslēgta)
#     lines_list2 = f.writelines() # ierakstīt līnijas kā listu
#     print(lines_list2)
# =============================================================================
    
    f.close() # labāk ir aiztaisīt ciet (aiztaisīt savienojumu), lai nav lieku gļuku
    
# f = open('demofile.txt', rt) # rt is the default value and means - read a text file (dont have to specify)

