lyst = []

for i in range(90):
    lyst.append(i)

for i in range(45):
    if (2*i) in lyst:
        lyst.remove(2*i)

for i in range(30):
    if (3*i) in lyst:
        lyst.remove (3*i)

for i in range(18):
    x = 5*i + 1
    if x in lyst:
        lyst.remove(x)

for i in range(10):
    x = 9*i + 5
    if x in lyst:
        lyst.remove(x)

for i in range(9):
    x = 10*i + 9
    if x in lyst:
        lyst.remove(x)

for i in range(5):
    x = 18*i + 13
    if x in lyst:
        lyst.remove(x)

print(lyst)

