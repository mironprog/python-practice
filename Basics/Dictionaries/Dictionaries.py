# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to acces a value quickly

capitals = {'USA':'Washington DC', 
            'India': "New delhi",
            'China':'Beijing',
            'Hungary':'Budapest'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()


print(capitals['Hungary'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key,value)