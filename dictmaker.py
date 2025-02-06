# coding=utf-8
"""
This python script generates a new words_dictionary.json from words_alpha.txt
This script aims to replicate the javascript equivalent.

Requires Python 3 preferably 3.4.4 (as this is the version it was built and tested on).

Algorithm extracted from original js code for use in constructing python script:
Import fs module (file system)
Set path constants

print to console "reading file" + SOURCE_PATH

open file given by SOURCE_PATH with utf8 encoding and define a callback function as a input
The callback function is called when the reading operation has finished with 2 parameters: 
1st input is error information and 2nd is the file contents.

Inside callback function:
    If error, throw error
    
    print to console "processing word list..."
    
    split file content by newline ('\n') -> reduce array into a single value using parameters: callback function and initial value (a empty dictionary)
        The callback function is defined to take 3 parameters and is run for each element in the array (2 are required):
        1st parameter: variable which is intialised by the inputted initial value and 
        previously returned value of the callback function. In this case the variable is a dictionary.
        2nd parameter: current element. In this case the string of a file line.
        3rd parameter (Optional): array index of the current element
        
        Inside callback function:
            retrieve word by converting the file line to string and remove leading & trailing whitespace characters
            create entry in dictionary using word as key and 1 as value
            return dictionary which is used for storage on the next run of callback function
    (final dictionary of words is returned and stored in a local variable)
        
    print to console 'writing dictionary to ' + OUTPUT_PATH + ' ...'
    
    get json string of dictionary
    write json string to file given by OUTPUT_PATH using uft8 encoding    
"""
import json

# Define input and output paths
SOURCE_PATH = './words_alpha.txt'
OUTPUT_PATH = './words_dictionary.json'

dictionary = {}

print("reading file {:s}".format(SOURCE_PATH))
with open(SOURCE_PATH, 'r', encoding='utf8') as input_file:
    print('processing word list...')

    for line in input_file:
        word = line.strip()
        dictionary[word] = 1

print('writing dictionary to {:s} ...'.format(OUTPUT_PATH))
with open(OUTPUT_PATH, 'w', encoding='utf8') as json_file:
    json.dump(dictionary, json_file, sort_keys=True)

print('done!')
