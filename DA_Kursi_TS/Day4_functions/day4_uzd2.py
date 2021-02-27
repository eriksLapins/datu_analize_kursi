
# my version
ievads = input("Lūdzu ievadiet simbolu virkni, kas ir 10-20 simbolus gara un ar lielajiem burtiem\n")

def simboli(simbols):
    if 10<=len(simbols)<=20 and simbols.isupper() == True: # principā varētu likt pēdējo '==' vietā is, 
                                                            # vai vispār nodzēst beigu daļu un rakstīt
                                                            # tikai simbols.isupper()
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(simboli(ievads))

#%% other version

def check_string(to_check):
    if len(to_check) >= 10 and len(to_check) <= 20 and to_check == to_check.upper():
        return True
    else:
        return False

def check_string2(to_check):
    if len(to_check) >= 10 and len(to_check) <= 20 and to_check.isupper() == True:
        return True
    else:
        return False

def check_string3(to_check):
    if len(to_check) >= 10 and len(to_check) <= 20 and to_check.isupper() is True:
        return True
    else:
        return False

def check_string4(to_check):
    if len(to_check) >= 10 and len(to_check) <= 20 and to_check.isupper():
        return True
    else:
        return False

# vajadzētu likt arī false, jo:
    
# slikts piemērs, bet nu:

def check_string5(to_check):
    if 10 <= len(to_check) <= 20 and to_check.isupper():
        return True


a = check_string5("AAAAAAAAAAAAaaa")

print(a) # outputs ir none (nav vērtības vispār) un tad var rasties problēmas, piemēram

if a:
    print("Viss ok")
else:
    print("Nav labi")


def check_string6(to_check):
    if len(to_check) >= 10 and len(to_check) <= 20 and to_check.isupper():
        return True
    return False # principā var bez else, šajā gadījumā

def check_string7(to_check):
    True if 10<=len(to_check)<=20 and to_check.isupper() else False

def check_string7(to_check):
    return 10<=len(to_check)<=20 and to_check.isupper()

