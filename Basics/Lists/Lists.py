# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hot-dog", "spaghetti", "pudding"]

food[0] = "sushi"

print(food[0])

food.append("ice cream")
food.remove("hot-dog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()

for x in food:
    print(x)