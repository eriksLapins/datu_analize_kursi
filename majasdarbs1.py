def vardu_minesana():
    lietotajs1 = input("Lietotāj 1, lūdzu ievadiet kādu vārdu!\n")
    hints = input("Lietotāj 1, lūdzu ievadiet kādu hintu!\n")
    
    lietotajs2 = input(f"Lietotāj 2, lūdzu uzminiet lietotāja 1 ievadīto vārdu, izmantojot hintu:\n \"{hints}\"\n")
    
    if lietotajs2 == lietotajs1:
        print("Uzvarēja 2. lietotājs!")
    else:
        print("Uzvarēja 1. lietotājs!")
        
if __name__ == '__main__':
    vardu_minesana()
