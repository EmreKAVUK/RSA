import math
p = int(input("P value "))
q = int(input("q value "))
e = int(input("e value "))
m = int(920)


gc = math.gcd(e,(p-1)*(q-1))
if gc != 1:
    exit()

def modInverse(a,m):

    a= a%m
    for x in range(1,m):
        if((a*x)%m ==1 ):
            print(x)
            return x
    return 1

def encryp():
    en = m ** (e) % (p*q)
    return en
def decreyp():
    en = int(encryp())
    inv = int(modInverse(e,(p-1)*(q-1)))
    de = (en**inv) % (p*q)
    print(de)


decreyp()