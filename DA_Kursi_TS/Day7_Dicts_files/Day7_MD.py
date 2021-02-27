# tikai lietotājs izvēlas kad iziet

# izvēles - 
# izveidot sarakstu, 
# pievienot jaunu elementu, 
# izdzēst no saraksta pēc indeksa, 
# izdzēst no saraksta pēc vērtības
# atrast elementu (search - ja ievadītais students atrodas sarakstā, tad izvadīt kārtas numuru(indeksu))
# iziet

# ierakstīt sarakstu failā

# ja nav ievadīta vērtība, un vēlas izvadīt/dzēst vai atrast - izvadīt kļūdas paziņojumu, ka saraksts ir tukšs
def uzdevums1():
    student_list = ['Jānis', 'Juris', 'Anna', 'Katrīna']
    while True:
        choice = input("""Ko jūs vēlaties darīt?\n
                       - izvadīt sarakstu (show list)\n
                       - pievienot elementu (add element)\n
                       - izdzēst no saraksta pēc elementa indeksa (delete by index)\n
                       - izdzēst no saraksta pēc vērtības (delete by value)\n
                       - atrast elementu (find element)\n
                       - ierakstīt visu sarakstu failā (wtf)\n
                       - iziet (exit)\n""")
        if choice.lower() == "exit":
            break
        
        elif choice.lower() == "show list":
            print(student_list)
        
        elif choice.lower() == "add element":
            new_student = input("Ievadiet studenta vārdu!\n")
            if new_student == "":
                print("Jūs neievadījāt studenta vārdu")
            else:
                student_list.append(new_student)
                
        elif choice.lower() == "delete by index":
            index_delete = input("Kuru indeksu vēlaties dzēst?\n")
            if index_delete == "":
                print("saraksts ir tukšs")
            else:
                student_list.pop(int(index_delete))
                
        elif choice.lower() == "delete by value":
            value_delete = input("Kuru vērtību vēlaties dzēst?\n")
            if value_delete == "":
                print("saraksts ir tukšs")
            else:
                student_list.remove(value_delete)
        
        elif choice.lower() == "wtf":
            f = open(str(input("Lūdzu ievadiet faila nosaukumu!\n")+'.txt'), 'w', encoding='utf-8')
            students_export = []
            
            for i in range(len(student_list)):
                students_export.append(str(student_list[i] + '\n'))
            f.writelines(students_export)
            f.close()
        
        elif choice.lower() == "find element":
            find_element = input("Kādu elementu vēlaties atrast?\n")
            if find_element == "":
                print("saraksts ir tukšs")
            else:
                for i in range(len(student_list)):
                    if student_list[i] == find_element:
                        print(f'Jūsu izvēlētais students ir {i}. pēc kārtas')
                    else:
                        continue
        else:
            print("Šādu darbību nesaprotu")
            
if __name__ == "__main__":
    uzdevums1()
