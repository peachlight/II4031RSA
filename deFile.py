def deRSA (m,n,d):
    for idx, c in enumerate(m):
        m[idx] =  (c**d) % n
    return m

f = open("nKey.pub",'r')
nKey = f.read()
n = int(nKey)
f.close()

f = open("priKey.pri",'r')
priKey = f.read()
d = int(priKey)
f.close()

f = open("tes.png",'rb')
m = bytearray(f.read())
m = deRSA(m,n,d)
f.close()

f = open("tes.png",'wb')
f.write(m)
f.close()
