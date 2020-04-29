from tkinter import *
import time
def button_clicked():
    # изменяем текст кнопки
    button['text'] = time.strftime('%H:%M:%S')
root=Tk()
root.geometry('300x400+300+200')
# создаём виджет
button = Button(root)
button1 = Button(root)
button1.place(x=10,y=10)
# конфигурируем виджет после создания
button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)

# также можно использовать квадратные скобки:
# button['text'] = time.strftime('%H:%M:%S')
# button['command'] = button_clicked
button.pack()
root.mainloop()