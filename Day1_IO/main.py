# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:59:50 2021

@author: Eriks.Lapins
"""
#%% hello world!
if __name__ == '__main__': # __name__ refers to the filename
    question1 = 'Kā jūs sauc?'
    
    print(question1)
    answer = input()
    
    question2 = 'Kāds ir jūsu vecums?' # ieteicams atstāt tā paša tipa vērtību uz vienu mainīgo (str, int, float, etc.)
    print(question2) # ja nepieciešamā vērtība ir nepieciešama tikai vienā vietā, tad labāk ir rakstīt šo vienreizējo vērtību printā
    # ja nepieciešams izmantot vērtību atkārtoti, tad ievietot mainīgajā
    
    result = question1 + " " + question2 
    print(result)

#%% working with inputs
# input will show the output anyway, but if you assign it to a variable, it will only show the output when you call the variable
if __name__ == '__main__': # __name__ refers to the filename
    print("Būs jautājumi!") # it is good to always put a print in the beginning
    question1 = 'Kā jūs sauc?'
    
    print(question1)
    answer = input()
    
    question2 = 'Kāds ir jūsu vecums?\n'
    answer2 = input(question2) # ja liek uzreiz inputā question2 (mainīgo), tad vajag pēc tā teksta ievietot \n, lai atbildi dod jaunā rindā
    
#%% Additional comments

if __name__ == '__main__':
    print("Kā jūs sauc?")
    firstName = input() # automātiski pārkonvertēs uz stringu, ja grib ciparu, tad jāieliek iekš int(input()) vai float(input())
    print("Sveiki, " + firstName + "!")