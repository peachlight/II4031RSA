def turnIntoASCII (input):
    temp = []
    for huruf in input:
        temp.append(ord(huruf))
    
    return temp

def enRSA (c,n,e):
    for idx, m in enumerate(c):
        c[idx] =  (m**e) % n
    return c

def deRSA (m,n,d):
    for idx, c in enumerate(m):
        m[idx] =  (c**d) % n
    return m

f = open ("nKey.pub","r")
nKey = f.read()
n = int(nKey)
f.close()

f = open ("pubKey.pub","r")
pubKey = f.read()
e = int(pubKey)
f.close()

f = open("priKey.pri","r")
priKey = f.read()
d = int(priKey)
f.close()

m = str(input("masukan kata: "))
list_m = turnIntoASCII(m)
list_m = enRSA(list_m,n,e)

hasilE = ''
hasilD = ''
for i in range (len(list_m)):
    hasilE += str(hex(list_m[i]))

print(hasilE)

list_c = deRSA(list_m,n,d)

for i in range(len(list_c)):
    hasilD += str(chr(list_c[i]))

print(hasilD)