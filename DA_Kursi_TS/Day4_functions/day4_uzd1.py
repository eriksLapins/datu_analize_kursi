# my version
def kapinatajs(baze,pakape):
    x = 1

    for i in range(pakape):
        x = baze*x
        
    print(x)

if __name__ == "__main__":
    kapinatajs(4, 5)

# other version

def power(base, power):
    result = 1
    
    for i in range(power):
        result *= base
        
    return result # drošāk likt result nevis print, lai nejūk kopā funkcijas
                    # vai ja nu grib šo vērtību izmantot nevis parādīt

if __name__ == "__main__":
    print(power(4, 5))
    print(pow(4, 5))