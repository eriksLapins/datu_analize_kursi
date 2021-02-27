#%% my version
# 1) uztaisīt funkciju, kurā padod vienu mianīgo - kas būs rindu skaits, kas failā būs jāģenerē.
# 2) Tiek ģenerēti random skaitļi - vienā rindā ir 6 random skaitļi no 1-10.
# 3) Tāds rindu skaits, kas ir padots ar parametru, tik rindas ir jāuztaisa.
# 4) Tas viss ir jāsaglabā failā

import random

def create_list(row_count):
    list_rows = []
    for i in range(row_count):
        list_numbers = []
        for i in range(6):
            list_numbers.append(random.randint(1,10))
        list_rows.append(str(list_numbers)+'\n')
    return list_rows

def write_to_file(file_name, list_to_write):
    f = open(str(file_name + '.txt'), 'w')
    f.writelines(list_to_write)
    f.close

if __name__ == "__main__":
    row_count = int(input("Cik rindas vēlaties uztaisīt?\n"))
    file_name = input("Lūdzu nosauciet failu!\n")
    full_list = create_list(row_count)
    write_to_file(file_name, full_list)

#%% other version
import random

def generate_file(count):
    lst_rows = []
    for i in range(count):
        result = ""
        for j in range(6):
            result += str(random.randint(1,10)) + ','
        result = result.rstrip(',')
        result += '\n'
        lst_rows.append(result)
    f = open('task2.txt', 'w')
    f.writelines(lst_rows)
    
    
if __name__ == "__main__":
    generate_file(4)