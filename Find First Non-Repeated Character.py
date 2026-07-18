# Find First Non-Repeated Character

text = input("Enter a Word: ")

for t in text:
    if text.count(t) == 1:
        print(f"First Non-Repeated Character: {t}")
        break

    else:
        print("No non-repeated character found.")
        break

