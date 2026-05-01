#Swap two variables without using a third variable.
a=20
b=30
print("The value of a is " + str(a))
print("The value of b is " + str(b))

a = a+b
b = a-b
a = a-b
print("after Swapping")
print("The value of a is " + str(a))
print("The value of b is " + str(b))