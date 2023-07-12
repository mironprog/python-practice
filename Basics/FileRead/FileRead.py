try:
    with open('C:\\Users\\bmare\\OneDrive\\Desktop\\Miron\\code\\python-practice\\Basics\\FileRead\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!")
