import json
mydict= {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
with open('words_alpha.txt') as txt:
    validWords = set(txt.read().split())
for words in validWords:
    mydict[words[0]].append(words)
mydict = json.dumps(mydict, indent=2)
with open('letter_wise_dictionary.json', 'a') as json:
    json.write(mydict)



