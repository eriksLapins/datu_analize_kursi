
def uzdevums_1():
    nr_of_inputs = int(input("Cik elementus vēlaties ievadīt?\n"))
    input_list = []
    
    for i in range(nr_of_inputs):
        input_list.append(input(f"Lūdzu ievadiet elementu {i+1}\n"))
    
    x = 0
    for i in range(len(input_list)):
        x += len(input_list[i])
    
    return round(x/len(input_list))

print(uzdevums_1())