#this is the Dictionary Practice code
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}   
print("Initial Dictionary:", my_dict)
# Accessing values by keys
print("Name:", my_dict["name"])  # Alice
print("Age:", my_dict.get("age"))  # 30
# Adding a new key-value pair
my_dict["job"] = "Engineer"
print("After adding job:", my_dict)
# Updating an existing value
my_dict["age"] = 31
print("After updating age:", my_dict)
# Removing a key-value pair
removed_value = my_dict.pop("city")
print("After removing city:", my_dict)
print("Removed city value:", removed_value)
# Looping through keys
print("Keys in the dictionary:")
for key in my_dict.keys():
    print(key)
# Looping through values
print("Values in the dictionary:")
for value in my_dict.values():
    print(value)
# Looping through key-value pairs
print("Key-Value pairs in the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value) 
# Checking if a key exists
if "name" in my_dict:
    print("Name key exists in the dictionary.")
# Getting the length of the dictionary
length_of_dict = len(my_dict)
print("Length of the dictionary:", length_of_dict)
# Clearing the dictionary
my_dict.clear()
print("After clearing the dictionary:", my_dict)
# Re-initializing the dictionary for further operations
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# Using setdefault to add a key-value pair if the key does not exist
my_dict.setdefault("country", "USA")
print("After using setdefault for country:", my_dict)
# Merging another dictionary
another_dict = {"age": 32, "hobby": "painting"}
my_dict.update(another_dict)
print("After merging another dictionary:", my_dict) 
# Copying the dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)
# Getting a value with a default if the key does not exist
favorite_color = my_dict.get("favorite_color", "blue")  
print("Favorite Color:", favorite_color)
# Using dictionary comprehension to create a new dictionary
squared_numbers = {x: x**2 for x in range(5)}
print("Squared Numbers Dictionary:", squared_numbers)
# Nested dictionary
nested_dict = { 
    "person1": {"name": "Bob", "age": 25},
    "person2": {"name": "Carol", "age": 28}
}
print("Nested Dictionary:", nested_dict)
# Accessing nested dictionary values
print("Person1's Name:", nested_dict["person1"]["name"])  # Bob
print("Person2's Age:", nested_dict["person2"]["age"])  # 28
# Removing an item using del
del my_dict["hobby"]
print("After deleting hobby:", my_dict)
# Using popitem to remove the last inserted item
last_item = my_dict.popitem()
print("After popitem:", my_dict)
print("Popped item:", last_item)
# Final state of the dictionary
print("Final Dictionary State:", my_dict)
# End of Dictionary Practice code
