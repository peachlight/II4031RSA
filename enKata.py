def turnIntoASCII (input):
    temp = []
    for huruf in input:
        temp.append(ord(huruf))
    
    return temp

def enRSA (c,n,e):
    for idx, m in enumerate(c):
        c[idx] =  (m**e) % n
    return c

f = open ("nKey.pub","r")
nKey = f.read()
n = int(nKey)
f.close()

f = open ("pubKey.pub","r")
pubKey = f.read()
e = int(pubKey)
f.close()

m = str(input("masukan kata: "))
list_m = turnIntoASCII(m)
list_m = enRSA(list_m,n,e)
# print(c)


# f = open("tes.png","rb")
# c = bytearray(f.read())
# c_fix = enRSA(c,n,e)
# f.close()

# f = open("tes.png","wb")
# f.write(c_fix)
# f.close()
