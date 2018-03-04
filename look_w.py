import itertools, os
from pathlib import Path

# Geting users home directory
h_path = str(Path.home()) # + any addtional path to a folder that contain word.txt

# Change directory to h_path where words.txt is located
os.chdir(h_path)

# Open words.txt
wor = open("words.txt","r")
wor = [x[:-1] for x in wor]

# Looking words that in the words list
# by number of letters and alphabets
def look_w(word,num):
    
    # Getting words list according to number of letters 
    mx = [wor[x] for x in range(len(wor)) if len(wor[x]) <= num] 
    
    # Create list of words that using itertools from the letters
    # and listing all words that relate to the word's letters.
    a = []
    b = {word[c]:word.count(word[c]) for c in range(len(word))}
    for ele in  itertools.product(word,repeat = num):
        d = {ele[c]:ele.count(ele[c]) for c in range(len(ele))}
        z=[]
        for i in d:
            try:
                v = len(d)
                if d[i] <= b[i]:
                    z.append('ok')
            except:
                pass
            finally:
                if v == len(z):
                    a.append("".join(ele))
    
    # Matching the created list words with the words in MX 
    # (words list from words.txt) and gather the valid words
    a = sorted(list(set(a[i] for i in range(len(a)) if a[i] in mx or a[i].capitalize() in mx)))
    return a
