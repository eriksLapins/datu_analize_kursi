#%% Task 1

def task1():
    place_of_living = input('Ievadiet dzīvesvietu!\n')
    print("Jūsu dzīvesvieta ir " + place_of_living)


if __name__ == '__main__':
    task1()

#%% functions

def integer_sample():
    sample_number = int(input("Ievadiet skaitli!\n")) # ar int() norāda, ka inputs būs integers
    print(sample_number)

def float_sample():
    sample_number = float(input("Ievadiet skaitli ar komatu!\n")) # ar float() norāda, ka inputs būs floats
    print(sample_number)

def to_string_sample():
    sample_number = float(input("Ievadiet skaitli ar komatu!\n"))
    print(str(sample_number) + " abc") # ar str() kovertē uz string'u

if __name__ == '__main__':
    to_string_sample()
#%% additional stuff

if __name__ == '__main__':
    a = "aa"
    b = "bb"
    c = 4
    print((a, b)*2) # izprintē 2x - kas līdzīgs ciklam
    
#%% Scope

# =============================================================================
#     
# if __name__ == "__main__":
#     
#     a = 3
#     print(a)
#     
#     a = "aa"
#     print(a)
#     
#     print(a+4) # shows error
# =============================================================================


def var_sample():
    a = "aa"
    print(a)
    
if __name__ == "__main__":
    
    a = 3
    print(a)
    
    var_sample()
    
    print(a+4) # prints 7 since 'a' in the function is local for the function
    
#%% if

def if_sample():
    # izvadīt "**", ja cilvēka ievadītā vērtība ir lielāka par 5, ja ne, tad izvadīt "*"
    personal_input = int(input("Lūdzu ievadiet skaitli!\n"))
    if personal_input > 5:
        print("**")
    else:
        print("*")
    
    string_input = input("Ievadiet vārdu:\n")
    if string_input == "aa":
        print("**")
    else:
        print("*")

if __name__ == "__main__":
    if_sample()

#%%

def if_sample2():
    # lietotajs ievada skaitli, parbaudit vai sis skaitlis ir diapozona no 1 lidz 10
    personal_input = int(input('Ievadiet skaitli'))
    if personal_input > 0 and personal_input < 11: # var arī 0 < personal_input < 11
        print('Skaitlis ir diapozonā')
    else:
        print('Nav diapozonā')

if_sample2()

#%%

def if_sample3():
    # lietotajs ievada skaitli, parbaudit vai sis skaitlis nav diapozona no 1 lidz 10
    personal_input = int(input('Ievadiet skaitli'))
    
    if personal_input < 1 or personal_input > 10: # var arī 0 < personal_input < 11
        print('Nav diapozonā')
    else:
        print('Ir diapozonā')

if_sample3()

#%% another extra

def task3():
    number1 = int(input("Ievadiet 1. skaitli!\n"))
    number2 = int(input("Ievadiet 2. skaitli!\n"))
    
    choice = input("Ievadiet + vai -")
    
    if choice == "+":
        print("Summa: " + str(number1 + number2))
    elif choice == "-":
        print("Starpība: " + str(number1 - number2))
    else:
        print("Kļūda!!!")

if __name__ == '__main__':
    task3()



