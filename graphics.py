from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import detecteyes
import numpy as np
import cv2
from cv2 import VideoCapture


root=Tk()
root.title("MRCS ThermoTower")
root.iconbitmap('D:/Projects/Spring2022/Learn/tkinter/icon_Ws5_icon.ico')
root.geometry('700x600')
root.configure(bg="black")

Label(root,text="MRCS",font=("times new roman",30,"bold"),bg="black",fg="white").pack()

#Processed Frame
f1=LabelFrame(root,bg="white")
f1.pack()

L1=Label(f1,bg="white")
L1.pack()

#Original Frame
f2=LabelFrame(root,bg="white")
f2.pack()

L2=Label(f1,bg="white")
L2.pack()


vid = VideoCapture(0)
while True:
    frame=vid.read()[1]
    #cv2.imshow('Eyes frame',frame)
    
    oimg=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    oimg=ImageTk.PhotoImage(Image.fromarray(oimg))
    L2['image']=oimg
    
    
    
    img=detecteyes.main(frame)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=ImageTk.PhotoImage(Image.fromarray(img))
    L1['image']=img


    

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    root.update()
vid.release()
cv2.destroyAllWindows()
    
