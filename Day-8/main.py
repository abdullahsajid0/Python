#this is the list practice file for day 8
fruits = ["apple", "banana", "cherry", "date"]
# Print the original list
print("Original list:", fruits) 
# Accessing elements by index
print("First fruit:", fruits[0])  # apple
print("Last fruit:", fruits[-1])  # date
# Slicing the list  
print("Fruits from index 1 to 3:", fruits[1:3])  # ['banana', 'cherry']
# Adding an element to the end of the list  
fruits.append("elderberry")
print("After appending elderberry:", fruits)
# Inserting an element at a specific position
fruits.insert(1, "blueberry")
print("After inserting blueberry at index 1:", fruits)
# Removing an element by value
fruits.remove("date")
print("After removing date:", fruits)
# Popping an element by index
popped_fruit = fruits.pop(2)
print("Popped fruit:", popped_fruit)
print("After popping index 2:", fruits)
# Finding the index of an element
index_of_banana = fruits.index("banana")
print("Index of banana:", index_of_banana)
# Counting occurrences of an element
fruits.append("apple")
apple_count = fruits.count("apple")
print("Number of apples in the list:", apple_count)
# Sorting the list
fruits.sort()
print("Sorted list:", fruits)
# Reversing the list
fruits.reverse()
print("Reversed list:", fruits)
# Getting the length of the list
length_of_list = len(fruits)
print("Length of the list:", length_of_list)
# Looping through the list
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)
# Clearing the list
fruits.clear()
print("After clearing the list:", fruits)