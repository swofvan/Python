# You are managing a small grocery store. You keep lists of items sold in three sections: fruits, vegetables, and beverages.
# Create separate lists for each section with at least 3 items.
# Add a new item to the fruits list.
# Insert a new item at the second position of the vegetables list.
# Remove the last item from the beverages list.
# Combine all three lists into a nested list called inventory.
# Use slicing to print only the first two fruits.
# Use negative indexing to access the last item from the vegetables list.
# Create a list of lengths of all items in the fruits list using list comprehension.
# Check if "Water" is in the beverages list.
# Finally, create a tuple of the first item from each section.

fruits = ["apple", "banana", "orange"]
vegetables = ["tomato", "potato", "onion"]
beverages = ["Juice", "Shake", "Coffie"]

fruits.append("Grape")
print(fruits)

vegetables.insert(1, "cabbage")
print(vegetables)

beverages.pop()
print(beverages)

inventory = [fruits, vegetables, beverages]
print(inventory)

print(fruits[:2])

print(vegetables[-1:])

lengths = [len(x) for x in fruits]
print(lengths)

if "Water" in beverages:
   print("Yes")
else:
   print("No")

first_item = (fruits[0], vegetables[0], beverages[0])
print(first_item) 