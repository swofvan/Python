# You are helping a shopper manage their grocery shopping list.
# Your task is to create a simple Python program that does the following steps in order:

# Initial Grocery List:
# Create a list with the initial items: ["milk", "bread", "eggs"].
# Add Item Function:
#   Write a function add_item(item) that adds a given item (string) to the grocery list.
# Remove Last Item Function:
#   Write a function remove_last_item() that removes the last item from the grocery list.
# Lambda Function for Display:
# Use a lambda function to print each item in the list with the format: "Item: <item>".
# Recursive Character Count (Bonus):
# Write a recursive function count_characters(items) that returns the total number
# of characters in all item names combined. For example, ["milk", "bread"] has 4 + 5 = 9 characters..


initial_items = ["milk", "bread", "eggs"]
print(initial_items)

def add_item(item):
    initial_items.append(item)
    print(initial_items)

add_item("butter")

def remove_last_item():
    initial_items.pop()
    print(initial_items)

remove_last_item()

show_items = lambda item: print("item : ", item)

for i in  initial_items:
  show_items(i)

def count_characters(items):
   if not items:
      return 0
   return len(items[0]) + count_characters(items[1:])

total_char = count_characters(initial_items)
print("Character Count: ", total_char)