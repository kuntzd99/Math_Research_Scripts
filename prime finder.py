def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
    

for i in range(1, 10000000000):
    if ((2**7) - 1) % i == 0:
        if isPrime(i):
            print(i)

##for i in range(1, 360):
##    if 360 % i == 0:
##        print(i)
