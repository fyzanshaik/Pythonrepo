from random import randint
num = randint(1, 1000) #picks random number from 1-1000

print(num)
xyz = num % 2
if xyz == 0:
    print("Even")
else:
    print("Odd")
