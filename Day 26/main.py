import pandas

# Creates a pandas DataFrame using the info in the csv file
alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

# Creates a new dictionary from the information in the DataFrame. The row indexes correspond to the letter and its
# corresponding NATO value
nato_dict = {row.iloc[0]: row.iloc[1] for (index, row) in alphabet.iterrows()}

# Asks the user to input any word
word = input("Enter a word: ").upper()

# Creates a new list with the NATO letters that correspond to the letters in the user's word
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)
