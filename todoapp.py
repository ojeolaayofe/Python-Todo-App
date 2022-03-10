from tkinter import *
from tkinter import messagebox
task_list = []
counter = 1
def inputError():
    if enterTaskField.get() == "":
        messagebox.showinfo("Input Error","Provide above your statement")
        return 0
    return 1
def insertTask():
    global counter
    value = inputError()
    if value == 0:
        return
    content = enterTaskField.get() + "\n"
    task_list.append(content)
    TextArea.insert('end -1 chars', "[" + str(counter) + "]" + content)
    counter +=1
    clear_insert()
def clear_insert():
    enterTaskField.delete(0, END)

def delete():
    global counter
    if len(task_list) == 0:
        messagebox.showerror("Delete Status","The Taskbox is empty")
        return
    number = taskNumberField.get(1.0,END)
    if number == "\n":
        messagebox.showerror("Input status","The number typed is not correct")
    else:
        task_no = int(number)
    clear_insert()
    task_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0,END)

    for i in range(len(task_list)):
        TextArea.insert('end -1 chars',"[" + str(i+1) + "] " + task_list[i])

if __name__=="__main__":
    root = Tk()
    root.configure(background='light green')
    root.title("Todo App")
    root.geometry("300x300")

    #================== Labels,entry goes here========================================
    enterTask = Label(root,text="Enter your task here",bg='light green',fg="black", font=("arial",16,'bold'))
    enterTaskField = Entry(root)
    submit = Button(root,text="Submit",bg='light green',fg="black",command=insertTask)

    TextArea = Text(root,height=5,width=25)
    taskNumber =Label(root,text="Delete With Task Number",bg="light green",fg="black")
    taskNumberField = Text(root,height=1,width=4)
    delete = Button(root,text="Delete",bg='light green',fg="black", command=delete)
    # =====================Data-Positions===============================================
    enterTask.grid(row=0,column=2)
    enterTaskField.grid(row=1, column=2)
    submit.grid(row=2, column=2,pady=10)
    TextArea.grid(row=3,column=2,padx=20,sticky=W)
    taskNumber.grid(row=4,column=2, pady=5)
    taskNumberField.grid(row=5,column=2)
    delete.grid(row=6,column=2,pady=10)
    root.mainloop()