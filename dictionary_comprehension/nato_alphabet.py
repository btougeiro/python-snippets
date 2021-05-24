import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = { row.letter:row.code for (_, row) in data_frame.iterrows() }

def generate_phonetic():    
    word = input("Enter a word: ").upper()
    try:
        result = [ nato_alphabet[letter] for letter in word ]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
