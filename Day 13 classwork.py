# You are helping a small stationery shop owner manage a simple list of items.

# First, ask the user to enter the name of a new item.
# If the file items.txt does not exist, create it and write the item into it.
# If the file exists, open it in append mode and add the new item.
# After writing, display the full list of items from the file to the user

new_item = input("Enter Item: ")

item = open("items.txt", "a")
item.write(new_item)
item.close()

item = open("items.txt", "r")
print(item.read())