from tkinter import *

root=Tk()
root.geometry("600x400")
root.title("Exploring Dictionary in Python")

label_mutable=Label(root)
label_immutable=Label(root)
label_tkinter=Label(root)

def mutable():
    label_mutable['text']="Has the ability to be changed."
    
def immutable():
    label_immutable['text']="Does not have the ability to be changed."
    
def tkinter():
    label_tkinter['text']="Is a GUI library in python language."
    
    
btn1=Button(root, text="meaning of mutable", command=mutable)
btn1.place(relx=0.5, rely=0.3, anchor=CENTER)
label_mutable.place(relx=0.5, rely=0.4, anchor=CENTER)

btn2=Button(root, text="meaning of immutable", command=immutable)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
label_immutable.place(relx=0.5, rely=0.6, anchor=CENTER)

btn3=Button(root, text="meaning of tkinter", command=tkinter)
btn3.place(relx=0.5, rely=0.7, anchor=CENTER)
label_tkinter.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()