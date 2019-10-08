STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        text = file.read()
        text = text.lower
        punct_table = str.maketrans({key: None for key in string.punctuation})
        text = text.translate(punct_table)
        words = text.split()
        STOP_WORDS_table = str.maketrans({key:None for key in STOP_WORDS})
        words_to_keep = words.translate(STOP_WORDS_table)
        # setdefault(key,1)
        print(words_to_keep)
        # pass


# - remove punctuation
# myString.translate(string.maketrans("",""), string.punctuation)

# - normalize all words to lowercase
# # string.lower

# - remove "stop words" -- words used so frequently they are ignored
# import string

# s = "string. With. Punctuation?"
# table = str.maketrans({key: None for key in string.punctuation})
# new_s = s.translate(table) 

# - go through the file word by word and keep a count of how often each word is used

# setdefault(key[, default])
# If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.

# d[key] = value
# Set d[key] to value.

# key in d
# Return True if d has a key key, else False.

# list(d)
# Return a list of all the keys used in the dictionary d.

# python3 word_frequency.py seneca_falls.txt

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
