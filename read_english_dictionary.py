import json
import os, sys

def load_words():
    try:
        filename = os.path.join(os.getcwd(), "words_dictionary.json")
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print(english_words["fate"])
