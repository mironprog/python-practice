from tkinter import *


count = 0
def click():
    global count
    count += 1
    print("You clicked the button")
    print(count)

window = Tk()

photo = PhotoImage(file='C:/Users/bmare/OneDrive/Desktop/Miron/code/python-practice/Basics/Buttons/heart.png')

button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()