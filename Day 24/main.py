# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Reads the starting text and saves it in variable 'contents'
with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()

# Reads the invited guests and stores them in a list called 'name_list'
# 'splitlines() is more concise as it simultaneously removes the \n character, but 'readlines()' was the example used in the course
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

new_name_list = []

# Removes the newline character from each name and stores the corrected names in a new list
for name in name_list:
    new_name_list.append(name.strip())

# For each name in the new list, replaces the '[name]' field with the appropriate name. Saves the resulting
# letter/string into a new file
for name in new_name_list:
    letter = contents.replace("[name]", name)
    file_path = f"Output/ReadyToSend/letter_to_{name}.txt"
    with open(file_path, mode="w") as new_file:
        new_file.write(letter)







