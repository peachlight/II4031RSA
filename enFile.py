def enRSA (c,n,e):
    for idx, m in enumerate(c):
        c[idx] =  (m**e) % n
    return c

def deRSA (m,n,d):
    for idx, c in enumerate(m):
        m[idx] =  (c**d) % n
    return m

# f = open("nKey.pub",'r')
# nKey = f.read()
# n = int(nKey)
# f.close()

# f = open("pubKey.pub",'r')
# pubKey = f.read()
# e = int(pubKey)
# f.close()

# f = open("tes.png",'rb')
# c = bytearray(f.read())
# c = enRSA(c,n,e)
# f.close()

# f = open("tes.png",'wb')
# f.write(c)
# f.close()
