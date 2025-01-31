import tkinter
from tkinter import*
root=Tk()
input=Entry(root,width=50)
input.grid(row=0,column=0,columnspan=3,padx=15,pady=15)


#Display function
def ToDisplay(num):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(num))
    

#All Clear function
def clear():
    input.delete(0,END)
    

#Addition
def add():
    num1=input.get()
    global f
    global choice
    choice="addition"
    f=int(num1)
    input.delete(0,END)
    

#Subtraction
def sub():
    num1=input.get()
    global f
    global choice
    choice="subtraction"
    f=int(num1)
    input.delete(0,END)
    

#Multiplication
def multiply():
    num1=input.get()
    global f
    global choice
    choice="multiply"
    f=int(num1)
    input.delete(0,END)


#Division
def divide():
    num1=input.get()
    global f
    global choice
    choice="divide"
    f=int(num1)
    input.delete(0,END)
    

#Delete function
def delete():
    current=input.get()
    input.delete(len(current)-1)
    

#Equal to function
def equal():
    num2=input.get()
    input.delete(0,END)
    if(choice=="addition"):
        input.insert(0,f+int(num2))
    elif(choice=="subtraction"):
        input.insert(0,f-int(num2))
    elif(choice=="multiply"):
        input.insert(0,f*int(num2))
    elif(choice=="divide"):
        input.insert(0,f/int(num2))
    
    
#Buttons
button1=Button(root,text="1",padx=50,pady=25,command=lambda:ToDisplay(1))
button2=Button(root,text="2",padx=50,pady=25,command=lambda:ToDisplay(2))
button3=Button(root,text="3",padx=50,pady=25,command=lambda:ToDisplay(3))
button4=Button(root,text="4",padx=50,pady=25,command=lambda:ToDisplay(4))
button5=Button(root,text="5",padx=50,pady=25,command=lambda:ToDisplay(5))
button6=Button(root,text="6",padx=50,pady=25,command=lambda:ToDisplay(6))
button7=Button(root,text="7",padx=50,pady=25,command=lambda:ToDisplay(7))
button8=Button(root,text="8",padx=50,pady=25,command=lambda:ToDisplay(8))
button9=Button(root,text="9",padx=50,pady=25,command=lambda:ToDisplay(9))
button0=Button(root,text="0",padx=50,pady=25,command=lambda:ToDisplay(0))
buttonAC=Button(root,text="AC",padx=45,pady=25,command=clear)
button_add=Button(root,text="+",padx=50,pady=25,command=add)
button_sub=Button(root,text="-",padx=50,pady=25,command=sub)
button_del=Button(root,text="del",padx=45,pady=25,command=delete)
button_mul=Button(root,text="X",padx=50,pady=25,command=multiply)
button_div=Button(root,text="/",padx=50,pady=25,command=divide)
button_equ=Button(root,text="=",padx=105,pady=25,command=equal)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_del.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
button_div.grid(row=5,column=2)
buttonAC.grid(row=6,column=0)
button_equ.grid(row=6,column=1,columnspan=2)
root.resizable(False,False)
root.mainloop()