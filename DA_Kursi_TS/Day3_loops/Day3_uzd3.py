#%% my version

def stars():
    x = ''
    for i in range(5):
        x = x + '*'
        print(x)
        
if __name__ == '__main__':
    stars()
    
#%% other version

def task3_1():
    stars = ""
    
    for i in range(5): # šoreiz svarīgi ir tas, cik reizes mēs ejam cauri
        stars = stars + "*"
        print(stars)
        
    
if __name__ == '__main__':
    task3_1()
    
#%% more easy other version

def task3_2():
    for i in range(1, 6):
        print('*' * i)

if __name__ == '__main__':
    task3_2()
    
#%% to reverse

def task3_3():
    for i in range(5, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    task3_3()
    
#%% alternative to reverse

def task3_3():
    for i in reversed(range(1, 6)):
        print('*' * i)

if __name__ == '__main__':
    task3_3()

#%% eglite

n = int(input("Ievadiet eglītes augstumu "))
z = n - 1
x = 1
for i in range(n):
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1