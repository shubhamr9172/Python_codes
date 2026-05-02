

# Create a list of 5 numbers and print the first and last element.
Students = ["Shubham", "Suyash", "Krishna", "Shital"]
print(Students[0])
print(Students[-1])
print()

# Add a new element at the end of a list.
Students.append("Jivan")
print(Students)
print()

# Remove an element from a list.
Students.remove("Shital")
print(Students)
print()

# Find the length of a list.
print(len(Students))
print()

# Check if a number exists in a list.
print("Check if a number exists in a list.")
num = [1, 2, 3, 4, 5]
if 2 in num:
    print("2 is in the list.")
else:
    print("2 is not in the list.")

print()
# Find the sum of all elements in a list.
print("Find the sum of all elements in a list.")
sum = 0
for i in num:
    sum = sum + i
print("The sum of all elements in the list is:", sum)
print()

#Find the maximum and minimum element.
min =num[0]
max =num[0]

for i in num:
    if i<min:
        min =i

for i in num:
    if i>max:
        max=i
print("Find the maximum and minimum element")
print("Minimum Number", min)
print("Maximum Number", max)

#Reverse a list (without using built-in reverse).

print()
print("Reverse a list (without using built-in reverse)")
num2 = [1,2,3,4,5]
reversed_list = []
for i in range(len(num2)-1,-1,-1):
    reversed_list.append(num2[i])
print(num2)
print(reversed_list)

#Count how many times a number appears.
print()
print("Count how many times a number appears")
num3 =[1,2,2,2,3,4,5,6]
count = 0
for i in num3:
    if i==2:
        count = count +1
print("2 is repating " + str(count) + " times in the list.")

#Print only even numbers from a list.
print()
print("Print only even numbers from a list.")
num4 = [1,2,3,4,5,6,7,8,9,10]
for i in num4:
    if i %2 == 0:
        print(i)