#%% my version
# uztaisīt tā, lai lietotājs ievada informāciju par studentu, jāsagatavo vārdnīca un jāizvada informācija
# visa ievade un izvade notiek main funckijā, bet visa loģika - vārdnīcas sagatavošana un atgriešana notiek citā failā

from day7_uzd1_logic import create_dict_student


def create_student():
    
    student_name = input("Lūdzu ievadiet studenta vārdu!")
    student_surname = input("Lūdzu ievadiet studenta uzvārdu")
    student_course = int(input("Lūdzu ievadiet studenta kursu"))
    student = create_dict_student(student_name, student_surname, student_course)
    
    return student

if __name__ == '__main__':
    print(create_student())

    
#%% other version
import day7_uzd1_logic as stParse

if __name__ == "__main__": # ievadīt inputus var arī bez atsevišķas funkcijas
    name = input("Lūdzu ievadiet studenta vārdu!")
    last_name = input("Lūdzu ievadiet studenta uzvārdu")
    course = int(input("Lūdzu ievadiet studenta kursu"))
 
    student_dict = stParse.create_student_dict(name, last_name, course)

    for key, val in student_dict.items(): # .items() is used to look for keys AND values, we ask for what we want
                                            # .values() - get values
                                            # .keys() - get keys
        print(key + ": " + str(val))
