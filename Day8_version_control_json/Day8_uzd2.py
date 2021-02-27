#%% my version

# 1) lasīt failu no iepriekšējā uzdevuma
# 2) izvadīt vidējo vērtību katrai rindai, summu katrai rindai
# 3) vidējo vērtību un summu no visiem skaitļiem



def list_sum_avg(file_path):
    f = open(file_path, 'r')
    file_lines = []
    for position, line in enumerate(f):
        file_lines.append(line.lstrip('[').rstrip("]\n"))
    
    sums_of_lines = []
    averages_of_lines = []
    total_sum = 0
    total_count = 0
    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i].split(', ')
        sum_numbers = 0
        
        for j in file_lines[i]:
            sum_numbers += int(j)

        total_sum += sum_numbers
        sums_of_lines.append(sum_numbers)
        averages_of_lines.append(sum_numbers/len(file_lines[i]))
        total_count += len(file_lines[i])
    
    total_average = total_sum/total_count
    
    return total_sum, sums_of_lines, averages_of_lines, total_average

    f.close()

    
if __name__ == "__main__":
    file_path = 'cipari.txt'
    total_sum, sums_of_lines, averages_of_lines, total_average = list_sum_avg(file_path)
    print(sums_of_lines)
    print(averages_of_lines)

    print(total_average)
    print(total_sum)
    
#%% other version - with string lines, not lists as strings
def read_file():
    f = open('task1.txt', 'r')
    file = f.readlines()
    
    total = 0
    num_count = 0
    
    for i in range(len(file)):
        file[i] = file[i].rstrip(',\n') # jo galā ir komats un enter
        num_list = file[i].split(',')
        num_count = 6 * len(file)

        line_sum = 0
        for val in num_list:
            line_sum += int(val)
        total += line_sum
        print(line_sum)
        print(line_sum/len(num_list))
        print("—————————————————————")
    
    print("Total - ")
    print(total)
    print(total/num_count)
        
if __name__ == "__main__":
    read_file()