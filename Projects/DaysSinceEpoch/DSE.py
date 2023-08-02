import time

print("This program will tell how much time passed since my computer thinks time started")

print(str(round(time.time()))+" seconds passed since epoch")
print(str(round(time.time()/60))+" minutes passed since epoch")
print(str(round(time.time()/3600))+" hours passed since epoch")
print(str(round(time.time()/86400))+" days passed since epoch")
print(str(round(time.time()/604800))+" weeks passed since epoch")
print(str(round(time.time()/31449600))+" years passed since epoch")

print("hehe")
