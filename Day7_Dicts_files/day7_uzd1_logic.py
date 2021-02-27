# my version
def create_dict_student(name, last_name, course):
    
    dictionary_students = {
            "studentName": name,
            "studentLastName": last_name,
            "course": course
        }
    
    return dictionary_students

#%%
# other version
def create_student_dict(name, last_name, course):
    students = {'name': name, 'lastName': last_name, 'course': course}
    return students