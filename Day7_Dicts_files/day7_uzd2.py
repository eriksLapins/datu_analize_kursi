#%% my version
# 1) paņemt txt failu no pielikuma
# 2) atvērt teksta failu un ielasīt listā
# 3) ar for cikla palīdzību (neizmantojot reverse, utt.) apgriezt listu otrādi
# 4) uztaisīt jaunu failu ar Python palīdzību un ierakstīt tajā listu


def reverse_list(filename):
    f = open(str(filename + '.txt'), 'r', encoding='utf-8')
    list_lines = f.readlines()
    new_list = []
    n_f = open(str(filename + '_otradi.txt'), 'w', encoding='utf-8')
    for i in range(len(list_lines)-1, -1, -1):
        new_list.append(list_lines[i])
    n_f.writelines(new_list)
    f.close()
    n_f.close()

if __name__ == "__main__":
    reverse_list('eglite')
    
#%% other version

def read(filepath):
    f = open(filepath, 'r', encoding = 'utf-8')
    file_list = f.readlines()
    f.close()
    return file_list

def write(filepath, poem_list):
    f = open(filepath, 'w', encoding = 'utf-8')
    rev = []
    for i in range(len(poem_list)-1, -1, -1):
        rev.append(poem_list[i])
    f.writelines(rev)
    f.close()

if __name__ == "__main__":
    poem = read('eglite.txt')
    write('eglite2.txt', poem)