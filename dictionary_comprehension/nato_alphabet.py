import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = { row.letter:row.code for (_, row) in data_frame.iterrows() }

word = input("Enter a word: ").upper()

result = [ nato_alphabet[letter] for letter in word ]

print(result)
