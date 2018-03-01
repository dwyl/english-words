# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:48:31 2018

@author: karja
"""

import itertools, os

# locate your folder that contain words.txt
os.chdir("C:\\Users\\user")

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
                if d[i] == b[i]:
                    z.append('ok')
            except:
                pass
            finally:
                if v == len(z):
                    a.append("".join(ele))
    
    # Matching the created list words with the words in words.txt
    # and gather the the valid words
    a = [a[i] for i in range(len(a)) if a[i] in mx or a[i].capitalize() in mx]
    return a
