from tkinter import *
def Hello(event):
    print ("Yet another hello world")
def window_deleted():
    print ('Окно закрыто')
    root.quit() # явное указание на выход из программы
root=Tk()
root.title('Пример приложения')
root.geometry('500x400+300+200') # ширина=500, высота=400, x=300, y=200
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна
root.resizable(False, False) # размеры не могут быть изменены
btn = Button(root,                  
             text="Жми",       
             width=30,height=5,     
             bg="white",fg="black") 
btn.bind("<Button-1>", Hello)       
btn.pack()  
root.mainloop()

root1=Tk()
button1 = Button()
button1.pack() 
root.mainloop()