import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

def inp():
    word = input()
    try:
        ans = [phonetic_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Please use only letters from the alphabet!")
        inp()
    else:
        print(ans)

inp()


