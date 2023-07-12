# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Harry Potter", 16, "male")

print(student.count("Harry Potter"))
print(student.index("male"))

for x in student:
    print(x)

if "Harry Potter" in student:
    print("Harry Potter is here!")