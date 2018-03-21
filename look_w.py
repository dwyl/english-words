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
    
    # Checking total num against the total letters of word.
    if num <= len(word):
        
        # Getting words list according to number of letters 
        mx = [wor[x] for x in range(len(wor)) if len(wor[x]) == num]
        
        # Listing all words that relate to the word's letters.
        a = []
        b = {word[c]:word.count(word[c]) for c in range(len(word))}
        for ele in  mx:
            elec = ele.lower()
            d = {elec[c]:elec.count(elec[c]) for c in range(len(elec))}
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
                        a.append("".join(elec))
        
        # Sorted the words list
        a = sorted(list(set(a)))
        return a
    else:
       return "⚔ Exceeding total letters ⚔".upper() 
