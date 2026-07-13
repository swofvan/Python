# # Find Maximum Repeated Character

# text = input("Enter a Sentance: ")


# char = ""

# char_count = 0

# for t in text:
#     count = text.count(t)
    
#     if count > char_count:
#         char_count = count
#         char = t

# print(char)


text = input("Enter a Sentence: ")

max_char = ""
max_count = 0

for t in text:
    c = text.count(t)
    if c > max_count:
        max_count = c
        max_char = t

print(max_char)