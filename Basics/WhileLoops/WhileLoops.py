# while loop = a statement that will execure it's block of code,
#              as long as it's condition reamins true

name = None

while not name:
    name = input("Enter your name: ")

print("Hello "+name)