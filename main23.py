from tkinter import *
def Hello(event):
    print ("Yet another hello world")
root = Tk()
btn = Button(root,                  
             text="Жми",       
             width=30,height=5,     
             bg="white",fg="black") 
btn.bind("<Button-1>", Hello)       
btn.pack()                          
root.mainloop()


