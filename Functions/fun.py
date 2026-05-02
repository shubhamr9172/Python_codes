#Write a function to add two numbers.

def add(a,b):
    c = a+b
    return c

a=10
b=20
result = add(a,b)
print("Addition "+ str(result))


#Write a function to check even or odd

def even_odd(num):
    trigger = False
    if num % 2 ==0:
        trigger = True
    return trigger

num = 2
result = even_odd(num)
if result == True:
    print("Even")
else:
    print("ODD")


#Function to find square of a number.
print()
print("Function to find square of a number.")
def square(num):
    return num**2

num = 10
result = square(num)
print(f"Square of {num} is {result}")
    