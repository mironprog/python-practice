
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

studentst = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))


grade = lambda grades:grades[1]
students.sort(key = grade)

age = lambda ages:ages[2]
sorted_students = sorted(studentst, key=age)

for i in students:
    print(i)

for i in sorted_students:
    print(i)