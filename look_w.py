import os
from pathlib import Path

# Geting users home directory
h_path = str(Path.home()) # + any addtional path to a folder that contain word.txt

# Change directory to h_path where words.txt is located
os.chdir(h_path)

# Open words.txt.
words = open('words.txt').read().split()

def look_w(word,num):
    # Looking words that in the words list
    # by number of letters and alphabets
    if num <= len(word) and num != 0:
        return [w for w in words if len(w) == num and 
                all(w.lower().count(c) <= word.lower().count(c) for c in w.lower())] 
    else:
        return "⚔ Exceeding total letters ⚔".upper()

# Usage
print(look_w('insane', 6))  # prints ['inanes', 'insane', 'sienna']
