
# my version

def vardu_minesana():
    lietotajs1 = input("Lietotāj 1, lūdzu ievadiet kādu vārdu, kas ir vismaz 5 simbolus garš!\n")
    hints = input("Lietotāj 1, lūdzu ievadiet kādu hintu, kas ir vismaz 8 simbolus garš!\n")
    
    
    
    if len(lietotajs1) >= 5 and len(hints) >= 8:
        lietotajs2 = input(f"Lietotāj 2, lūdzu uzminiet lietotāja 1 ievadīto vārdu, izmantojot hintu:\n \"{hints}\"\n")
        if lietotajs2 == lietotajs1:
            print("Uzvarēja 2. lietotājs!")
        else:
            print("Uzvarēja 1. lietotājs!")

    elif len(lietotajs1) < 5 and len(hints) < 8:
        print('Spēle beidzās, jo gan hints, gan minamais vārds ir par īsu')        

    elif len(lietotajs1) < 5:
        print("Spēle beidzās, jo minamais vārds ir par īsu!")

    else:
        print("Spēle beidzās, jo hints ir par īsu!")
        
if __name__ == '__main__':
    vardu_minesana()