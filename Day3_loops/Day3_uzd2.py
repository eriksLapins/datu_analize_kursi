
def factorial():
    x = 1
    lietotaja_skaitlis = int(input('lūdzu ievadiet veselu skaitli!'))
    if lietotaja_skaitlis > 0:
        for i in range(1, lietotaja_skaitlis+1):
            x = x*i
        print(x)
    elif lietotaja_skaitlis == 0:
        print(1)
    else:
        print('Šim skaitlim nav faktoriāļa, jo tas ir negatīvs')


if __name__ == '__main__':
    factorial()