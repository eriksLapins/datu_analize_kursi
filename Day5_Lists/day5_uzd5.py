#%% my version
def uzd5(string_list, string_variable):
    index_list = []
    for i in range(len(string_list)):
        if string_variable == string_list[i]:
            index_list.append(i)
    if len(index_list) == 0:
        print("Šāda simbolu virkne nav sarakstā")
    return index_list

if __name__ == "__main__":
    my_list = ["aa", "bb", "cc", "aa", "bb", "cc", "dddd", "abcd", "abcd"]
    string_variable = "ab"
    print(uzd5(my_list, string_variable))
            
#%% other version

def search(string_list, item):
    found = False
    
    for i in range(len(string_list)):
        if item == string_list[i]:
            found = True
            print(i)

    if not found:
        print("Sarakstā šādas vērtības nav!")
        
if __name__ == "__main__":
    my_list = ["aa", "bb", "cc", "aa", "bb", "cc", "dddd", "abcd", "abcd"]
    string_variable = "aa"
    search(my_list, string_variable)
            