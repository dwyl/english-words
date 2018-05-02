# Open words.txt.  Assumes words.txt is in same folder as look_w.py
words = open('words.txt').read().split()


def look_w(word, num):
    # Looking words that in the words list
    # by number of letters and alphabets
    return [w for w in words if len(w) == num and
            all(w.lower().count(c) <= word.lower().count(c) for c in w.lower())]


# Usage
print(look_w('insane', 6))  # prints ['inanes', 'insane', 'sienna']
print(look_w('quit', 3))    # prints ['ITU', 'qui', 'Tiu', 'tui', 'UIT', 'uti']
print(look_w('quit', 4))    # prints ['quit']
print(look_w('cake', 99))   # prints []
