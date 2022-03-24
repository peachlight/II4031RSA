from math import sqrt
import random

def isPrima(bilangan) -> bool:
    cek = 0
    if(bilangan > 1):
        if bilangan != 2:
            for i in range(2, int(sqrt(bilangan)) + 1):
                if (bilangan % i == 0):
                    cek = 1
                    break
    else:
        cek = 1
    return cek == 0

def tenE (p,q):
    phi = (p-1)*(q-1)
    list_e = []

    for i in range (2,phi):
        if phi % i != 0:
            if isPrima(i):
                list_e.append(i)
    
    e = random.choice(list_e)
    return e

def modInverse(a, n):
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if t < 0:
        t = t + n
    return t

def tenD (p,q,e):
    phi = (p-1)*(q-1)
    d = modInverse(e, phi)
    return d

p = int(input("masukan p: "))
cek_p = False
while not(cek_p):
    if isPrima(p):
        cek_p = True
    else:
        print("input p bukan prima")
        p = int(input("masukan p: "))
    

q = int(input("masukan q: "))
cek_q = False
while not(cek_q):
    if isPrima(q):
        cek_q = True
    else:
        print("input q bukan prima")
        q = int(input("masukan q: "))

e = tenE(p,q)
d = tenD(p,q,e)

e_fin = str(e)
d_fin = str(d)

print(e_fin,d_fin)

f = open('pubKey.pub',"w")
f.write(e_fin)
f.close

f = open('priKey.pri','w')
f.write(d_fin)
f.close