import json
import os, sys

def load_words():
    try:
        filename = os.path.dirname(sys.argv[0])+"\\"+"words_dictionary.json"
        with open(filename,"r") as enlish_dictionary:
            valid_words = json.load(enlish_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print(english_words["fate"])
