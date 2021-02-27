#%% MD1 - Vardu Minesanas Spele

def vardu_minesana():
    lietotajs1 = input("Lietotāj 1, lūdzu ievadiet kādu vārdu, kas ir vismaz 5 simbolus garš!\n")
    hints = input("Lietotāj 1, lūdzu ievadiet kādu hintu, kas ir vismaz 8 simbolus garš!\n")
    for i in range(20):
        print('')
    
    
    
    if len(lietotajs1) >= 5 and len(hints) >= 8:
        allowed_tries = 5
        tries = 0
        while True:
            if tries < allowed_tries:
                lietotajs2 = input(f"Lietotāj 2, lūdzu uzminiet lietotāja 1 ievadīto vārdu, izmantojot hintu:\n \"{hints}\"\nJums ir atlikuši {allowed_tries-tries} mēģinājumi\n")

                if lietotajs2 == lietotajs1:
                    print("Uzvarēja 2. lietotājs!")
                    break
                else:
                    tries = tries + 1
                    if tries < allowed_tries:
                        print('Lūdzu miniet vēlreiz')
                    else:
                        continue 
            else:
                print("Maksimālais mēģinājumu skaits sasniegts, uzvarēja 1. lietotājs")
                break

    elif len(lietotajs1) < 5 and len(hints) < 8:
        print('Spēle beidzās, jo gan hints, gan minamais vārds ir par īsu')        

    elif len(lietotajs1) < 5:
        print("Spēle beidzās, jo minamais vārds ir par īsu!")

    else:
        print("Spēle beidzās, jo hints ir par īsu!")
        
if __name__ == '__main__':
    vardu_minesana()

#%% MD2 - Kalkulators

# my version
def calculator():
   

    while True:
        
        number1 = float(input('Lūdzu ievadiet vienu skaitli ar komatu\n'))
        number2 = float(input('Lūdzu ievadiet otru skaitli ar komatu\n'))
        action = input('Ko jūs vēlaties darīt ar šiem skaitļiem?\n ievadiet darbības simbolu\nProtu:\n -saskaitīt (+)\n -atņemt (-)\n -reizināt (*)\n -dalīt (/)\n -kāpināt (**)\n -modulo (%)\n')
        
        if action == '+':
            print(number1+number2)
        elif action == '-':
            print(number1+number2)
        elif action == '*':
            print(number1*number2)
        elif action == '/':
            print(number1/number2)
        elif action == '%':
            print(number1%number2)
        elif action == '**':
            print(number1**number2)
        else:
            print('Es šādu darbību nemāku :(')
        
        exit_calculator = input('Vai tas būtu viss? Ja teiksi \'yes\', tad iziesi!\n')
        
        if exit_calculator == 'yes':
            break
    

if __name__ == '__main__':
    calculator()
    
    
# other version


def homework_calculator():
    
    while True:
        number1 = float(input("Kādu skaitli vēlaties ievadīt?\n"))
        number2 = float(input("Kādu skaitli vēlaties ievadīt?\n"))
        
        choice = input("Ievadīt +,-,*, vai /")
        
        if choice == "+":
            print(number1+number2)
        elif choice == "-":
            print(number1-number2)
        elif choice == "*":
            print(number1*number2)
        elif choice == "/":
            print(number1/number2)
        else:
            print("Kļūda! Bija jāievada +,-,*, vai /")
        
        exit_calc = input("Vai vēlaties iziet? Ievadiet y, ja jā")
        if exit_calc.upper() == 'Y': # lai būtu konsistence atbildēs
            break
        
if __name__ == '__main__':
    homework_calculator()