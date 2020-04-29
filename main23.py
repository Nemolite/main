from tkinter import *
def Hello(event):
    print ("Yet another hello world")
    label1 = Label(text="Hello Python", fg="#eee", bg="#333")
    label1.pack()
root = Tk()
btn = Button(root,                  
             text="Жми",       
             width=30,height=5,     
             bg="white",fg="black") 
btn.bind("<Button-1>", Hello)       
btn.pack()                          
root.mainloop()


