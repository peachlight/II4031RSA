# Import Library & Extension
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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

# Add Function Generate Private Key
def generatePriv():
    #Call Function
    return()

# Add Function Generate Public Key
def generatePub():
    #Call Function
    return()

# Add Function for Encrypt
def encryptFile():
    dirPath = UploadAction()
    print(dirPath)
    INPUT = open(dirPath,'rb')
    # KUNCI = 
    # print(KUNCI)
    INPUT.close()

    #Encryption
    
    # Overwrite file
    f = open(dirPath,'wb')
    # f.write(kata)
    f.close

    # Message to label
    Output.delete("1.0","end")
    PRINTRESULT = open(dirPath,'rb')
    Output.insert(END, PRINTRESULT)
    PRINTRESULT.close()

# Add Function for Decrypt
def decryptFile():
    dirPath = UploadAction()
    print(dirPath)
    INPUT = open(dirPath,'rb')
    # KUNCI = 
    # print(KUNCI)
    INPUT.close()

    #Decryption
    
    # Overwrite file
    f = open(dirPath,'wb')
    # f.write(kata)
    f.close

    # Message to label
    Output.delete("1.0","end")
    PRINTRESULT = open(dirPath,'rb')
    Output.insert(END, PRINTRESULT)
    PRINTRESULT.close()

# Add Button, Label
l = Label(frame, text = "Upload file untuk didekripsi/enkripsi")
l.pack()
generatePrivKeyButton = tk.Button(frame, text = "Generate Private Key", padx=10, pady=5, fg="black", bg="white", command = generatePriv)
generatePrivKeyButton.pack(pady=10)
generatePubKeyButton = tk.Button(frame, text = "Generate Public Key", padx=10, pady=5, fg="black", bg="white", command = generatePub)
generatePubKeyButton.pack(pady=10)
encryptFileButton = tk.Button(frame, text = "Upload File and Encrypt", padx=10, pady=5, fg="black", bg="white", command = encryptFile)
encryptFileButton.pack(pady=10)
decryptFileButton = tk.Button(frame, text = "Upload File and Decrypt", padx=10, pady=5, fg="black", bg="white", command = decryptFile)
decryptFileButton.pack(pady=10)
Output = Text(frame, height = 5, width = 25, bg = "light cyan")
Output.pack()    

root.mainloop()