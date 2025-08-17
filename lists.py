import random

##[what_to_keep for item in list if condition]

number = [random.randint(1,10) for i in range(5)]
print(f"random Number genrated is {number}")
square = [num*num for num in number]
print(f"the square number is {square}")
