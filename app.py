# Import Library & Extension
import time, os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from enFile import *
from keyGen import *

# Import Function
"""from deFile import *
from deKata import *
from enFile import *
from enKata import *
from enkripdekrip import *
from keyGen import *
from rsa import *"""

# Tampilan Halaman Utama
root = tk.Tk()
root.title("RSA")
canvas = tk.Canvas(root, height=580, width=720, bg="#C0D1EB")
canvas.pack()

frame = tk.Frame(root, bg="#E1EAF7")
frame.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.05)

titleText = Text(frame, height=10, width=52)
labelTitle = Label(frame, text="Tugas 3 II4031 Kriptografi dan Koding")
labelTitle.config(font = ("Arial", 24))
labelTitle.pack()

pathh = Entry(root)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

# Add Function Upload File
def UploadAction(event=None):
    tf = filedialog.askopenfilename(initialdir="C:/Users/MainFrame/Desktop/",
        title="Select a File",
        filetypes=(("All Files", "*.*"),))
    pathh.insert(END, tf)
    return (tf)

# Add Function Generate  Key
def generateKey():
    #Call Function
    p = int(inputp.get("1.0", "end-1c"))
    cek_p = False
    if isPrima(p):
        cek_p = True
    else:
        print("input p bukan prima")
    q = int(inputq.get("1.0", "end-1c"))
    cek_q = False
    if isPrima(q):
        cek_q = True
    else:
        print("input q bukan prima")
    if cek_p and cek_q:
        n = p*q
        e = tenE(p,q)
        d = tenD(p,q,e)

        n_fin = str(n)
        e_fin = str(e)
        d_fin = str(d)

        f = open('nKey.pub',"w")
        f.write(n_fin)
        f.close

        f = open('pubKey.pub',"w")
        f.write(e_fin)
        f.close

        f = open('priKey.pri','w')
        f.write(d_fin)
        f.close
    return()

# Add Function for Encrypt Text
def encryptText():
    milprev = int(round(time.time()*1000))
    #Ambil Nilai N
    f = open("nKey.pub",'r')
    nKey = f.read()
    n = int(nKey)
    f.close()
    #Ambil Nilai pub key
    f = open("pubKey.pub",'r')
    pubKey = f.read()
    e = int(pubKey)
    f.close()

    dirPath = UploadAction()
    print(dirPath)
    INPUT = open(dirPath,'rb')
    # KUNCI = 
    # print(KUNCI)
    c = bytearray(INPUT.read())
    INPUT.close()

    #Encryption
    c = enRSA(c,n,e)
    
    # Overwrite file
    f = open(dirPath,'wb')
    f.write(c)
    f.close
    milcurr = int(round(time.time()*1000))

    size = str(os.path.getsize(dirPath))
    duration = str(milcurr-milprev)

    # Message to label
    Output.delete("1.0","end")
    PRINTRESULT = open(dirPath,'rb')
    Output.insert(END, PRINTRESULT)
    durationOutput.insert(END,duration+" ms")
    sizeOutput.insert(END,size+" bytes")
    PRINTRESULT.close()

# Add Function for Decrypt Text
def decryptText():
    milprev = int(round(time.time()*1000))
    #Ambil Nilai N
    f = open("nKey.pub",'r')
    nKey = f.read()
    n = int(nKey)
    f.close()
    #Ambil Nilai pri key
    f = open("priKey.pri",'r')
    priKey = f.read()
    d = int(priKey)
    f.close()

    dirPath = UploadAction()
    print(dirPath)
    INPUT = open(dirPath,'rb')
    m = bytearray(INPUT.read())
    # KUNCI = 
    # print(KUNCI)
    INPUT.close()

    #Decryption
    m = deRSA(m,n,d)

    # Overwrite file
    f = open(dirPath,'wb')
    f.write(m)
    f.close
    milcurr = int(round(time.time()*1000))

    size = str(os.path.getsize(dirPath))
    duration = str(milcurr-milprev)

    # Message to label
    Output.delete("1.0","end")
    PRINTRESULT = open(dirPath,'rb')
    Output.insert(END, PRINTRESULT)
    durationOutput.insert(END,duration+" ms")
    sizeOutput.insert(END,size+" bytes")
    PRINTRESULT.close()

# Add Function for Encrypt
def encryptFile():
    milprev = int(round(time.time()*1000))
    #Ambil Nilai N
    f = open("nKey.pub",'r')
    nKey = f.read()
    n = int(nKey)
    f.close()
    #Ambil Nilai pub key
    f = open("pubKey.pub",'r')
    pubKey = f.read()
    e = int(pubKey)
    f.close()

    dirPath = UploadAction()
    print(dirPath)
    INPUT = open(dirPath,'rb')
    # KUNCI = 
    # print(KUNCI)
    c = bytearray(INPUT.read())
    INPUT.close()

    #Encryption
    c = enRSA(c,n,e)
    
    # Overwrite file
    f = open(dirPath,'wb')
    f.write(c)
    f.close
    milcurr = int(round(time.time()*1000))

    size = str(os.path.getsize(dirPath))
    duration = str(milcurr-milprev)

    # Message to label
    Output.delete("1.0","end")
    PRINTRESULT = open(dirPath,'rb')
    Output.insert(END, PRINTRESULT)
    durationOutput.insert(END,duration+" ms")
    sizeOutput.insert(END,size+" bytes")
    PRINTRESULT.close()

# Add Function for Decrypt
def decryptFile():
    milprev = int(round(time.time()*1000))
    #Ambil Nilai N
    f = open("nKey.pub",'r')
    nKey = f.read()
    n = int(nKey)
    f.close()
    #Ambil Nilai pri key
    f = open("priKey.pri",'r')
    priKey = f.read()
    d = int(priKey)
    f.close()

    dirPath = UploadAction()
    print(dirPath)
    INPUT = open(dirPath,'rb')
    m = bytearray(INPUT.read())
    # KUNCI = 
    # print(KUNCI)
    INPUT.close()

    #Decryption
    m = deRSA(m,n,d)

    # Overwrite file
    f = open(dirPath,'wb')
    f.write(m)
    f.close
    milcurr = int(round(time.time()*1000))

    size = str(os.path.getsize(dirPath))
    duration = str(milcurr-milprev)

    # Message to label
    Output.delete("1.0","end")
    PRINTRESULT = open(dirPath,'rb')
    Output.insert(END, PRINTRESULT)
    durationOutput.insert(END,duration+" ms")
    sizeOutput.insert(END,size+" bytes")
    PRINTRESULT.close()

# Add Button, Label
l = Label(frame, text = "Masukkan nilai p dan q untuk generate key")
l.pack()
inputp = Text(frame, height = 2, width = 25, bg = "light yellow")
inputp.insert(END, "Masukkan nilai p")
inputp.pack()
inputq = Text(frame, height = 2, width = 25, bg = "light yellow")
inputq.insert(END, "Masukkan nilai q")
inputq.pack()
generateKeyButton = tk.Button(frame, text = "Generate Key", padx=10, pady=5, fg="black", bg="white", command = generateKey)
generateKeyButton.pack(pady=10)
encryptTextButton = tk.Button(frame, text = "Upload Text and Encrypt", padx=10, pady=5, fg="black", bg="white", command = encryptText)
encryptTextButton.pack(pady=10)
decryptTextButton = tk.Button(frame, text = "Upload Text and Decrypt", padx=10, pady=5, fg="black", bg="white", command = decryptText)
decryptTextButton.pack(pady=10)
encryptFileButton = tk.Button(frame, text = "Upload File and Encrypt", padx=10, pady=5, fg="black", bg="white", command = encryptFile)
encryptFileButton.pack(pady=10)
decryptFileButton = tk.Button(frame, text = "Upload File and Decrypt", padx=10, pady=5, fg="black", bg="white", command = decryptFile)
decryptFileButton.pack(pady=10)
durationLabel = Label(frame, text = "Durasi")
durationLabel.pack()
durationOutput = Text(frame, height = 1, width = 15, bg = "light yellow")
durationOutput.pack()
sizeLabel = Label(frame, text = "File Size")
sizeLabel.pack()
sizeOutput = Text(frame, height = 1, width = 15, bg = "light yellow")
sizeOutput.pack()
Output = Text(frame, height = 5, width = 25, bg = "light cyan")
Output.pack()    

root.mainloop()