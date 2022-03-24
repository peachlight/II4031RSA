from math import sqrt
import random

def turnIntoASCII (input):
    temp = []
    for huruf in input:
        temp.append(ord(huruf))
    
    return temp

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

def tenE (p,q):
    phi = (p-1)*(q-1)
    list_e = []

    for i in range (2,phi):
        if phi % i != 0:
            if isPrima(i):
                list_e.append(i)
    
    e = random.choice(list_e)
    return e

def tenD (p,q,e):
    phi = (p-1)*(q-1)
    d = modInverse(e, phi)
    return d

def enRSA (p,q,e,m):
    n = p*q
    
    c = (m**e) % n
    return c

def deRSA (p,q,d,c):
    n = p*q
    m = (c**d) % n
    return m

# kata = str(input("masukan kata: "))
# listKata = turnIntoASCII(kata)
hasil = []
listKata = [104, 158, 93, 14, 85]

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

# e = tenE(p,q)
# d = tenD(p,q,e)
e = 89
d = 41
print(listKata)
print(p)
print(q)
print(e)
print(d)
    
# for i in range (len(listKata)):
#     temp = enRSA(p,q,e,listKata[i])
#     hasil.append(temp)

for i in range (len(listKata)):
    temp = deRSA(p,q,d,listKata[i])
    hasil.append(temp)

print(hasil)