# def double(x):
#     return x * 2
# 
# print(double(5))

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False

print(double(5))
print(multiply(10,10))
print(add(1,2,3))
print(full_name("Mathias", "Rex"))
print(age_check(18))