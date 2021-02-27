# my version
def summa_starpiba():
    skaitlis1 = int(input("Ievadiet vienu veselu skaitli!\n"))
    skaitlis2 = int(input("Ievadiet otru veselu skaitli!\n"))
    izvele = input("Vai jūs vēlaties summu? (izvēlaties un ierakstiet vienu no diviem - yes/no) \n")
    if izvele == 'yes':
        print(f"Summa: {skaitlis1 + skaitlis2}")
    else:
        print(f"Starpība: {skaitlis1 - skaitlis2}")

if __name__ == '__main__':
    summa_starpiba()
    
# another version

def task3():
    number1 = int(input("Ievadiet 1. skaitli!\n"))
    number2 = int(input("Ievadiet 2. skaitli!\n"))
    
    choice = input("Ievadiet + vai -")
    
    if choice == "+":
        print("Summa: " + str(number1 + number2))
    else:
        print("Starpība: " + str(number1 - number2))

if __name__ == '__main__':
    task3()