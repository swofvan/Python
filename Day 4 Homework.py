# You are organizing participants for three different workshops in a coding bootcamp: Web Development, Data Science, and UI/UX Design.
# Create a list for each workshop containing the names of 3 participants.
# Combine all three workshop lists into a single nested list called all_participants.
# A new participant joins the Web Development workshop — add their name to that list.
# Insert one more participant at the 2nd position in the Data Science list.
# Remove the last participant from the UI/UX Design list.
# Copy the list of Data Science participants to a new list and clear the original.
# From the Web Development list, display only the first two participants.
# Use list comprehension to create a list of the length of each name in the copied Data Science list.
# Check whether “Asha” is in any of the workshop lists.
# Finally, create a tuple that stores the name of the first participant from each workshop list (use slicing and indexing as needed).

web_development = ["Raju", "Radha", "Anu"]
data_science = ["Lakshmi", "Akhila", "Swofvan"]
ui_ux_design = ["Jishnu", "Shihab", "Sufaid"]

all_participants = [web_development, data_science, ui_ux_design]
print(all_participants)

web_development.append("Bibin")
print(web_development)

data_science.insert(1,"Nikhil")
print(data_science)

ui_ux_design.pop()
print(ui_ux_design)

new_data_science = data_science.copy()
print(new_data_science)

data_science.clear()
print(data_science)

print(web_development[:2])

data_len = [len(x) for x in new_data_science]
print(data_len)

if "Asha" in all_participants :
    print("Yes, Asha Attented the workshop")
else :
    print("No, Asha didn't Attented the workshop")

tuple1 = (web_development[0], new_data_science[0], ui_ux_design[0])
print(tuple1)