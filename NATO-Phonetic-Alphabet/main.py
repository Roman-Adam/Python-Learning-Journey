
import pandas as pd

# Read the CSV file
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary using dictionary comprehension
phonetic_dict = {
    row.letter: row.code
    for (index, row) in data.iterrows()
}

# Ask the user to enter a word
word = input("Enter a word: ").upper()

# Convert each letter into its NATO phonetic code
output_list = [
    phonetic_dict[letter]
    for letter in word
    if letter in phonetic_dict
]

# Display the result
print(output_list)
