# scope = The region that a variable is recognized

name = "Michael" # global scope

def display_name():
    name = "Jackson" # local scope
    print(name)

display_name()
print(name)