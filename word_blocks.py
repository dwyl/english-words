### Gather a dictionary of all possible blocks of the following type:
### C blocks at beginning
### V blocks at end
### VC blocks at beginning
### VC blocks anywhere else
### CV words (as the entire word)
### Particularly common letter pairs (i.e. if some letter almost always appears next to some other letter).
### In all cases ignore the length of the block. Keep the number of occurrences, with an option to drop the entry if there are too few.

"""A script for gathering letter block statistics from a word list."""

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
    blocks["v_e"] = {} # vowels at end
    blocks["vc_b"] = {} # vowel/consonant at beginning
    blocks["vc_me"] = {} # vowel/consonant not at beginning
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
                # Count pure blocks
                if ws[j][0] in CONSONANTS:
                    if ws[j] not in blocks["c"]:
                        blocks["c"][ws[j]] = 1
                    else:
                        blocks["c"][ws[j]] += 1
                if ws[j][0] in VOWELS:
                    if ws[j] not in blocks["v"]:
                        blocks["v"][ws[j]] = 1
                    else:
                        blocks["v"][ws[j]] += 1

                ##############

            # Record V words
            if len(ws) == 1 and ws[0][0] in VOWELS:
                blocks["v_w"][word] = 1

            # Record CV words
            if len(ws) == 2 and ws[0][0] in CONSONANTS and ws[1][0] in VOWELS:
                blocks["cv_w"][word] = 1

    # Delete entries below threshold
    if threshold > 0:
        for key in blocks:
            # Skip whole-word lists
            if 'w' in key:
                continue
            for k in blocks[key]:
                if bocks[key][k] < threshold:
                    del blocks[key][k]

    # Load block dictionaries into INI file parser
    config = configparser.ConfigParser(allow_no_value=True)
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
               ";     v_e -- vowel at end\n" \
               ";     vc_b -- vowel/consonant at beginning\n" \
               ";     vc_me -- vowel/consonant not at beginning\n" \
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
    gather_blocks("words_alpha.txt", "word_blocks.ini", ub=100)

### Plan: Gather a list of all allowed syllables into an INI file (just gather the keys, no values).
### In the misspeller, after splitting the word, we gather clusters to make syllables, and then randomly replace some characters with other characters of the same type (with some special rules to keep some things grouped, like qu or th).
### Then we check the result against our list of whitelisted syllable structures to make sure that it's valid.
### The required probabilities would be the probabilities to transform any given character in any given part of the word, or maybe to simplify just the probability of transforming any given consonant or vowel (or maybe separately inserting or deleting, all of which would be mutually exclusive). Also consider rearranging the syllables of a word, accomplished by moving around VC blocks or just swapping one C block for another or one V block for another.
