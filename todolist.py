import tkinter
from tkinter import*
root=Tk()
root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False,False)
tasks=[]
def addTask():
    task=task_enter.get()
    task_enter.delete(0,END)
    if task:
        with open("taskslist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        tasks.append(task)
        listbox.insert(END,task)
def deleteTask():
    global tasks
    task=str(listbox.get(ANCHOR))
    if task in tasks:
        tasks.remove(task)
        with open("taskslist.txt",'w') as tasksfile:
            for task in tasks:
                tasksfile.write(task+"\n")
        listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global tasks
        with open("taskslist.txt","r") as taskfile:
            task_list=taskfile.readlines()
        for task in task_list:
            if task!='\n':
                tasks.append(task)
                listbox.insert(END,task)
    except:
        file=open('taskslist.txt','w')
        file.close() 
#icon image
icon_image=PhotoImage(file="todo.png")
root.iconphoto(False,icon_image)
#top bar
top_bar=PhotoImage(file="topbar1.png")
Label(root,image=top_bar,width=400,height=77).pack()
#note icon
note_image=PhotoImage(file="task.png")
Label(root,image=note_image,width=29,height=35).place(x=30,y=25)
heading=Label(root,text="TASKS",font="arial 20 bold",fg="white",bg="black")
heading.place(x=130,y=20)
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)
task=StringVar()
task_enter=Entry(frame,width=18,font="arial 20",bd=0)
task_enter.place(x=10,y=7)
task_enter.focus()
#ADD button
button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)
frame1=Frame(root,bd=3,width=700,height=280,bg="black")
frame1.pack(pady=(160,0))
listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="black",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
#delete button
delete_icon=PhotoImage(file="delete_img.png")
Button(root,image=delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
root.mainloop()