#%% MD1

# Ievada veselu skaitli - izvadīt skaitļu summu no 0 līdz cilvēka ievadītajam skaitlim
# Ja ievada 0, vai negatīvu skaitli, izvadīt kļūdas paziņojumu

number = int(input("Ievadiet skaitli\n"))

def number_row(skaitlis):
    if skaitlis > 0:
        for i in range(skaitlis+1):
            print(i)
    elif skaitlis <= 0:
        print('lūdzu ievadiet pozitīvu skaitli, kas ir lielāks par 0\n')
    
if __name__ == "__main__":
    number_row(number)


#%% MD2

# Izvadīt visus pāra skaitļus līdz 20

for i in range(20):
    if i%2 == 0:
        print(i)

#%% MD3

# Uztaisīt funkciju (var apvienot ar otro uzdevumu), kas kā parametrus paņem
# skaitli un boolean vērtību

# Skaitli izmantot kā maksimālo vērtību (ciklam) un ja booleans ir true, tad
# jāizvada pāra skaitļi, ja nav, tad jāizvada nepāra skaitļi

skaitlis = int(input("Lūdzu ievadiet skaitli"))
booleans = input("Lūdzu ievadiet True vai False")

def homework_3(number, boolean):
    if boolean.upper() == "TRUE":
        for i in range(number):
            if i%2 == 0:
                print(i)
    elif boolean.upper() == "FALSE":
        for i in range(number):
            if i%2 != 0:
                print(i)
    
if __name__ == "__main__":
    homework_3(skaitlis, booleans)

#%% MD4

# Uztaisīt tā, lai cilvēks ievada skaitļus līdz netiek ievadīts negatīvs skaitlis
# Ja ievada negatīvu skaitli, tad izbeigt ciklu, un izvadīt visu iepriekšējo summu.
# Ja cilvēks ievada pozitīvu skaitli, tad turpinam skaitīt


def counting_positives():
    x = 0
    while True:
        skaitlis = int(input("Lūdzu ievadiet skaitli"))
        if skaitlis >= 0:
            x += skaitlis
        else:
            return x
        
if __name__ == '__main__':
    print(counting_positives())