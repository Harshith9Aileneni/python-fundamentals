# 1. Write a function that takes a name and returns it in uppercase
name = "harshith"
age = 23
shift = 1
a = 2
b = 4
number = 6
def make_capital(name):
    answer = name.upper()
    print(answer)
    return answer
    # Fill this in based on what you learned in cipher project



# 3. Write a function using f-strings to format a message
def create_message(name, age):
    message = f"my name is {name} and my age is {age}"
    print(message)
    # Use f-strings like you learned in cipher
    return (message)



# 4. Function that takes two numbers and adds them
def add_numbers(a, b):

    result = a + b
    print(result)
    return result



# 5. Function that takes a word and returns its length
def word_length(name):
    length = len(name)
    print(length)
    return length

# 6. Function that checks if a number is even
def is_even(number):
    if number % 2 == 0 :
        print("even")
        return True
    else :
        print("odd")
        return False




make_capital(name)
create_message(name, age)
add_numbers(a, b)
word_length(name)
is_even(number)