lyst = []

lcm = 360

for i in range(lcm):
    lyst.append(i)

for i in range(lcm//2):
    x = 2*i
    if x in lyst:
        lyst.remove(x)

for i in range(lcm//3):
    x = 3*i
    if x in lyst:
        lyst.remove(x)

for i in range(lcm//5):
    x = 5*i
    if x in lyst:
        lyst.remove(x)

for i in range(lcm//9):
    x = 9*i + 7
    if x in lyst:
        lyst.remove(x)

for i in range(lcm//12):
    x = 12*i + 11
    if x in lyst:
        lyst.remove(x)

for i in range(lcm//36):
    x = 36*i + 1
    if x in lyst:
        lyst.remove(x)

print(lyst)

