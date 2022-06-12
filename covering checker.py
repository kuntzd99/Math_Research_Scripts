#
#
#

lyst = []

for i in range(288):
    lyst.append(i)

for i in range(144):
    if (2*i) in lyst:
        lyst.remove(2*i)

for i in range(96):
    if (3*i) in lyst:
        lyst.remove (3*i)

for i in range(72):
    x = 4*i
    if x in lyst:
        lyst.remove(x)

for i in range(36):
    x = 8*i
    if x in lyst:
        lyst.remove(x)

for i in range(32):
    if (9*i + 5) in lyst:
        lyst.remove(9*i + 5)

for i in range(24):
    x = 12*i + 11
    if x in lyst:
        lyst.remove(x)

##for i in range(18):
##    x = 16*i + 15
##    if x in lyst:
##        lyst.remove(x)

##for i in range(8):
##    if (18*i + 7) in lyst:
##        lyst.remove(18*i + 7)
##
##for i in range(6):
##    x  = 24*i + 17
##    if x in lyst:
##        lyst.remove(x)
##
for i in range(8):
    x = 36*i + 1
    if x in lyst:
        lyst.remove(x)

####for i in range(4):
####    x = 36*i + 31
####    if x in lyst:
####        lyst.remove(x)
####
##        
##for i in range(3):
##    x = 48 * i + 13
##    if x in lyst:
##        lyst.remove(x)
####
for i in range(6):
    x = 48 * i + 17
    if x in lyst:
        lyst.remove(x)

##for i in range(2):
##    x = 72*i + 29
##    if x in lyst:
##        lyst.remove(x)
##
##for i in range(2):
##    x = 72*i + 13
##    if x in lyst:
##        lyst.remove(x)
##

for i in range(2):
    x = 144*i + 7
    if x in lyst:
        lyst.remove(x)

for i in range(2):
    x = 144*i + 13
    if x in lyst:
        lyst.remove(x)

for i in range(2):
    x = 144*i + 85
    if x in lyst:
        lyst.remove(x)
        
print(lyst)
    
