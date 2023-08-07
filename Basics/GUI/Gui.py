from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Window")

icon = PhotoImage(file='C:/Users/bmare/OneDrive/Desktop/Miron/code/python-practice/Basics/GUI/bird.png')
window.iconphoto(True, icon)
window.config(background="black")

window.mainloop()
