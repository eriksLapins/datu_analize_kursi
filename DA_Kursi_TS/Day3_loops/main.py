# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:31:40 2021

@author: Eriks.Lapins
"""

#%% for loops

def for_loop_sample():
    for i in range(10): # i - skaitītājs (parasti lieto i, kā saīsinājumu vārdam iteration)
                            # vienmēr sāks skaitīt no 0
        print(i)
        
def for_loop_sample2():
    for i in range(1, 10): # lai norādītu, ka sākam ar 1
        print(i)

def for_loop_sample3():
    for i in range(0, 10, 2): # lai norādītu, ka ejam ik pa 2, bet vajag norādīt sākuma punktu
        print(i)
    else:
        print('viss') # ja nu sačakarējas ievadā

def for_loop_sample4():
    for i in range(10):
        print(i)
        x = i # strādā, bet parāda tikai pēdējo
    print("-------------")
    print(x)

def for_loop_sample5():
    x = 0 # lai strādātu "x + i"
    for i in range(10):
        print(i)
        x = x + i # nestrādā, jo nav pirmā reference. Šis katrā cikla iterācijā mainās (pieskaita klāt x'am i)
    print("-------------")
    print(x)

if __name__ == '__main__':
    # for i in range(3): # izprintēs 3 reizes
        for_loop_sample5()

#%% while loops

def while_sample():
    i = 0
    while i < 10:
        print(i)
        i += 1 # strādā arī ar stringiem

# var būt arī bezgalīgie cikli - piemēram temperatūras mērīšana, automātiskās durvis (visu laiku skatās, vai ir vai nav cilvēks)


if __name__ == '__main__':
    while_sample()
    
#%% endless while loop
def while_endless():
    while True:
        print(1)
        user_input = input('Vai vēlaties iziet?')
        
        if user_input == 'y':
            break # iziet no cikla
            # return # iziet no funkcijas
            # exit() # iziet no programmas
            # continue # aizies uz nākamo iterāciju
        print('Nenospieda y')
    print('Pēc metodes')
        
if __name__ == '__main__':
    while_endless()