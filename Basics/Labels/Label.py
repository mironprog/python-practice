from tkinter import *


window = Tk()

photo = PhotoImage(file='C:/Users/bmare/OneDrive/Desktop/Miron/code/python-practice/Basics/Labels/bird.png')

label = Label(window, 
              text="Hello World", 
              font=('Arial', 40, 'bold'), 
              fg='#00FF00', 
              bg='black',
              relief=SUNKEN,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound = 'bottom')
label.pack()
# label.place(x=100,y=100)


window.mainloop()