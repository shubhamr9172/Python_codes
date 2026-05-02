#Create a dictionary with name, age, city.
print("Create a dictionary with name, age, city")
Details ={
    "name" :"Shubham",
    "age" : 26,
    "city" : "Pune"
}
print(Details)

#Access and print a value using key.
print()
print("Access and print a value using key.")
print(Details["name"])

#Add a new key-value pair.
print()
print("Add a new key-value pair. Company = TCS")
Details["Company"] = "TCS"
print(Details)

#Update an existing value.
print()
print("Update an existing value. Company = Accenture")
Details["Company"] ="Accenture"
print(Details)


#Delete a key from dictionary.
print()
print("Delete a key from dictionary.")
Details.pop("Company")
print(Details)

#Looping through Dictionary
print()
print("Looping through Dictionary")
for key in Details:
    print(key, Details[key])


#Find the key with maximum value.

def max_key_find(d):
    if not d:
        return None
    max_key = None
    max_value = float('-inf')
    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

my_dict = {'a':10, 'b':20, 'c':30}
print(my_dict)
max_key = max_key_find(my_dict)
print(f"Key with max value : {max_key}")

#Merge two dictionaries.
print()
print("Merge two dictionaries.")
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}

merged= d1 | d2
print(merged)
#other way
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}

#Check if a key exists.
print()
print("Check if a key exists.")

d = {'a':1,'b':2,'c':3}
if 'b' in d:
    print("key Exist")
else:
    print("Key Does not exist")

#Check if a key exists.
print()
print("Check if a key exists.")

if 2 in d.values():
    print("Value Exist")
else:
    print("Value does not exist")