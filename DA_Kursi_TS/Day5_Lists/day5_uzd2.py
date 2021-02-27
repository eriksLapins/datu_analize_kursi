import random

def random_list():
    list_random = []
    sum_n = 0
    for i in range(5):
        n = random.randint(0, 10)
        list_random.append(n)
        sum_n += n
    if sum_n > 10:
        return f"** {list_random} {sum_n}"
    else:
        return f"* {list_random} {sum_n}"
    
if __name__ == "__main__":
    print(random_list())