"""A script for gathering letter block statistics from a word list.

Counts occurrences of contiguous blocks of consonants and vowels in various
parts of a word.
"""

import configparser
import re
import time

# Define global consonant and vowel lists
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"

#==============================================================================

def gather_blocks(fin, fout, lb=None, ub=None, threshold=0, comments=True):
    """gather_blocks(fin, fout[, lb][, ub][, threshold][, comments])
    Gathers particular types of letter blocks from a word list.

    Positional arguments:
    fin (str) -- name of input word list file
    fout (str) -- name of output statistic file

    Keyword arguments:
    [lb=None] (int) -- lower bound letter index (None to start at beginning)
    [ub=None] (int) -- upper bound letter index (None to process until end)
    [threshold=0] (int) -- minimum number of required instances for a substring
                           to be included in the statistics
    [comments=True] (bool) -- whether to include comments in the output INI
                              file to explain the naming convention behind the
                              sections

    The input file should consist of a dictionary text file, with a single word
    on each line.

    The output is an INI file with a section for letter block type, with each
    key/value pair representing a letter block and its frequency.
    
    The optional bounds can be used to process only a limited range of the word
    list. Every list index in the interval [lb,ub) is included. Setting either
    to None causes that bound to be ignored.
    """

    # Start timer
    start = time.time()

    # Define dictionary of dictionaries
    blocks = {}
    blocks["c"] = {} # consonants
    blocks["v"] = {} # vowels
    blocks["vc"] = {} # vowel/consonant
    blocks["c_b"] = {} # consonants at beginning
    blocks["v_w"] = {} # vowel-only words
    blocks["cv_w"] = {} # consonant/vowel entire words

    # Read word list line-by-line and record blocks
    with open(fin, 'r') as f:
        i = -1 # current word index
        for line in f:
            i += 1

            # Respect bounds
            if lb != None and i < lb:
                continue
            if ub != None and i >= ub:
                break

            # Get current word
            word = line.strip()

            # Break into consonant/vowel blocks
            ws = [x for x in re.split("(["+VOWELS+"]+)|(["+CONSONANTS+"]+)",
                                      word, flags=re.IGNORECASE) if x]

            # Classify block types
            for j in range(len(ws)):
                
                # Count consonant blocks
                if ws[j][0] in CONSONANTS:
                    if ws[j] not in blocks["c"]:
                        blocks["c"][ws[j]] = 1
                    else:
                        blocks["c"][ws[j]] += 1
                    # Count consonants at beginning
                    if j == 0:
                        if ws[j] not in blocks["c_b"]:
                            blocks["c_b"][ws[j]] = 1
                        else:
                            blocks["c_b"][ws[j]] += 1
                
                # Count vowel blocks
                if ws[j][0] in VOWELS:
                    if ws[j] not in blocks["v"]:
                        blocks["v"][ws[j]] = 1
                    else:
                        blocks["v"][ws[j]] += 1
                    # Count vowel words
                    if len(ws) == 1:
                        if ws[j] not in blocks["v_w"]:
                            blocks["v_w"][ws[j]] = 1
                        else:
                            blocks["v_w"][ws[j]] += 1

                # Move on only for counting pairs
                if j >= len(ws) - 1:
                    continue

                # Count vowel/consonant pairs
                if ws[j][0] in VOWELS and ws[j+1][0] in CONSONANTS:
                    if ws[j]+ws[j+1] not in blocks["vc"]:
                        blocks["vc"][ws[j]+ws[j+1]] = 1
                    else:
                        blocks["vc"][ws[j]+ws[j+1]] += 1

                # Count consonant/vowel words
                if (len(ws) == 2 and ws[j][0] in CONSONANTS
                    and word in VOWELS):
                    if word not in blocks["cv_w"]:
                        blocks["cv_w"][word] = 1
                    else:
                        blocks["cv_w"][word] += 1

            # Record V words
            if len(ws) == 1 and ws[0][0] in VOWELS:
                blocks["v_w"][word] = 1

            # Record CV words
            if len(ws) == 2 and ws[0][0] in CONSONANTS and ws[1][0] in VOWELS:
                blocks["cv_w"][word] = 1

    # Initialize INI file parser
    config = configparser.ConfigParser(allow_no_value=True)

    # Obey threshold
    if threshold > 0:
        # If using a threshold, reduce each block dictionary
        for key in blocks:
            # Always keep whole words
            if key == "v_w" or key == "cv_w":
                config[key] = blocks[key]
                continue
            # Otherwise keep only thresholded values
            dic = {} # temporary reduced dictionary
            for k in blocks[key]:
                if blocks[key][k] >= threshold:
                    dic[k] = blocks[key][k]
            config[key] = dic
            del dic
    else:
        # If no threshold, load blocks as-is
        for key in blocks:
            config[key] = blocks[key]

    # Write INI file
    with open(fout, 'w') as f:
        config.write(f)

    # Write comments
    if comments == True:
        # Define comment string
        com = "; Statistics generated from '" + fin + "'"
        if lb != None or ub != None:
            com += "(lines "
            if lb == None:
                com += "0 - "
            else:
                com += str(lb) + " - "
            if ub == None:
                com += str(i-1) + ")"
            else:
                com += str(ub-1) + ")"
        com += ".\n"
        if threshold > 0:
            com += "; Threshold: " + str(threshold) + "\n"
        com += ";\n; Each section below is a block of characters.\n" \
               "; The section names are as follows:\n" \
               ";     c -- consonants\n" \
               ";     v -- vowels\n" \
               ";     vc -- vowel/consonant\n" \
               ";     c_b -- consonant at beginning\n" \
               ";     v_w -- vowel-only words\n" \
               ";     cv_w -- consonant/vowel entire words\n\n"
        
        # Write comments to beginning of file
        with open(fout, 'r') as f:
            for line in f:
                com += line
        with open(fout, 'w') as f:
            f.writelines(com[:-1])

    # Report total time
    print("Processed '" + fin + "' after " + str(time.time() - start) +
          " seconds.")

#==============================================================================

# Automatically process dwyl dictionary
if __name__ == "__main__":
    gather_blocks("words_alpha.txt", "word_blocks.ini")
