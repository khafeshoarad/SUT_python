#this program is just a piece of cake
z = int(input())
gholam = int(input())
ghodrat = int(input())
def mf(y,x):
    while x != 0:
        carryover = y & x
        y = y ^ x
        x = carryover << 1
    return y
seyed = mf(z,gholam)
#cake is not real(vagei)
print(seyed)
if seyed == ghodrat :
    print('YES')
else :
    print('NO')