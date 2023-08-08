from tkinter import *

food = ["Pikza", "Hamburgir", "Hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered pizza!")
    elif(x.get() == 1):
        print("You ordered hamburger!")
    elif(x.get() == 2):
        print("You ordered hotdog!")
    else:
        print("huh?")

window = Tk()

pizzaImage = PhotoImage(file='C:/Users/bmare/OneDrive/Desktop/Miron/code/python-practice/Basics/RadioButtons/pizza.png')
hamburgerImage = PhotoImage(file='C:/Users/bmare/OneDrive/Desktop/Miron/code/python-practice/Basics/RadioButtons/hamburger.png')
hotdogImage = PhotoImage(file='C:/Users/bmare/OneDrive/Desktop/Miron/code/python-practice/Basics/RadioButtons/hotdog.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact',40),
                              image = foodImages[index],
                              compound = 'left',
                              indicatoron = 0,
                              width = 475,
                              command = order)
    
    radiobutton.pack(anchor=W)






window.mainloop()