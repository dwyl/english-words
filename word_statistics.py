"""A script for gathering letter distribution statistics from a word list.

The main public function, gather_stats(), can be used to gather letter
statistics for a given word list file and write the contents of the statistic
dictionaries to an INI file.

If run as a script, the default word list is the dwyl English word dictionary
"words_alpha.txt".
"""

import configparser
import time

# Define global consonant and vowel lists
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"

#==============================================================================

def gather_stats(fin, fout, lb=None, ub=None, threshold=0, empty=False,
                 alternate=True, comments=True):
    """gather_stats(fin, fout[, lb][, ub][, threshold][, empty][, alternate][,
                    comments])
    Gathers letter statistics from a given file.

    Positional arguments:
    fin (str) -- name of input word list file
    fout (str) -- name of output statistic file

    Keyword arguments:
    [lb=None] (int) -- lower bound letter index (None to start at beginning)
    [ub=None] (int) -- upper bound letter index (None to process until end)
    [threshold=0] (int) -- minimum number of required instances for a substring
                           to be included in the statistics
    [empty=False] (bool) -- whether to include empty statistic categories in
                            the output file (True to include all, False to skip
                            empty)
    [alternate=False] (bool) -- whether to include substrings that switch
                                between vowels and consonants more than once
                                (True to include all, False to exclude
                                substrings that alternate more than once)
    [comments=True] (bool) -- whether to include comments in the output INI
                              file to explain the naming convention behind the
                              sections

    The input file should consist of a dictionary text file, with a single word
    on each line.

    The output is an INI file with a section for each statistic, and with each
    key/value pair representing a letter (or letter combination) and its
    frequency.

    The optional bounds can be used to process only a limited range of the word
    list. Every list index in the interval [lb,ub) is included. Setting either
    to None causes that bound to be ignored.
    """
    
    # Due to the large number of statistics collected, the dictionaries are
    # organized in a multidimensional array whose elements are indexed as
    # follows:
    #
    #     stats[number][type][position]
    #
    # <number> -- 0 for single-letter statistics, 1 for letter pair statistics,
    #             2 for letter triple statistics, etc.
    # <type> -- 0 for all, 1 for consonants only, 2 for vowels only, 3 for
    #           consonant/vowel pairs (in that order), 4 for vowel/consonant
    #           pairs (in that order)
    # <position> -- 0 for anywhere, 1 for beginning, 2 for end, 3 for middle
    #
    # For example, stats[0][0][0] is the dictionary of all single letters
    # occurring anywhere in a word, while stats[3][2][2] is the dictionary of
    # all vowel pairs occurring at the end of a word.
    #
    # Note that types 3 and 4 (for consonant/vowel pairs) are only defined when
    # the number of letters is exactly 2. Entries of the form stats[n][3][p] or
    # stats[n][4][p] are empty unless n = 1.

    # Start timer
    start = time.time()

    # Define character arrays for use in naming the dictionaries
    dic_numbers = [str(i) for i in range(1, 6)]
    dic_types = ["_a", "_c", "_v", "_cv", "_vc"]
    dic_pos = ["_a", "_b", "_e", "_m"]

    # Define multidimensional array of statistic dictionaries
    stats = [[[{} for p in range(len(dic_pos))] for t in range(len(dic_types))]
             for n in range(len(dic_numbers))]
    
    # Read word list line-by-line and record statistics
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

            # Process each character
            for j in range(len(word)):
                # Determine if this is the beginning of the word
                beg = False
                if j == 0:
                    beg = True
                # Consider each valid substring length
                for num in range(1, min(len(word)-j+1, len(dic_numbers)+1)):
                    # Determine if this is the end of the word
                    end = False
                    if j + num >= len(word):
                        end = True
                    # Get the current substring
                    ss = word[j:j+num]
                    # Skip if alternating
                    if alternate == False and _alternating(ss) == True:
                        continue
                    # Determine the types of letters
                    cat = _categorize(ss) # set of valid type indices
                    for t in cat:
                        # All
                        if ss not in stats[num-1][t][0]:
                            stats[num-1][t][0][ss] = 1
                        else:
                            stats[num-1][t][0][ss] += 1
                        # Beginning
                        if beg == True:
                            if ss not in stats[num-1][t][1]:
                                stats[num-1][t][1][ss] = 1
                            else:
                                stats[num-1][t][1][ss] += 1
                        # End
                        if end == True:
                            if ss not in stats[num-1][t][2]:
                                stats[num-1][t][2][ss] = 1
                            else:
                                stats[num-1][t][2][ss] += 1
                        # Middle
                        if beg == False and end == False:
                            if ss not in stats[num-1][t][3]:
                                stats[num-1][t][3][ss] = 1
                            else:
                                stats[num-1][t][3][ss] += 1

    # Load statistic dictionaries into INI file parser
    config = configparser.ConfigParser(allow_no_value=True)
    for i in range(len(dic_numbers)):
        for j in range(len(dic_types)):
            for k in range(len(dic_pos)):
                # Skip if empty
                if empty == False and len(stats[i][j][k]) < 1:
                    continue
                # Skip entries below the threshold
                if threshold > 0:
                    for s in tuple(stats[i][j][k]):
                        if stats[i][j][k][s] < threshold:
                            del stats[i][j][k][s]
                # Otherwise load dictionary
                config[dic_numbers[i] + dic_types[j] + dic_pos[k]] = \
                                      stats[i][j][k]

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
        if empty == False:
            com += "; Empty fields excluded.\n"
        if alternate == False:
            com += "; Excluding alternating CVC and VCV sequences.\n"
        com += ";\n; Each section below is a dictionary of substring " \
               "frequencies.\n" \
               "; The section names have the format:\n" \
               ";     [<n>_<t>_<p>] \n" \
               "; where:\n" \
               ";     <n> -- length of substring\n" \
               ";     <t> -- letter type ('a' all, 'c' consonant only,\n" \
               ";            'v' vowel only, 'cv' consonant/vowel pair,\n" \
               ";            'vc' vowel/consonant pair\n" \
               ";     <p> -- position ('a' all, 'b' beginning, 'e' end,\n" \
               ";            'm' middle)\n\n"

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

def _categorize(s):
    """_categorize(s) -> set
    Determines the letter type category of a string.

    Positional arguments:
    s (str) -- string to categorize

    Returns:
    (set) -- set of type categories to which the string belongs (0 for any, 1
               for consonant only, 2 for vowel only, 3 for consonant/vowel
               pair, 4 for vowel/consonant pair)
    """

    # Verify that the string is not empty
    if len(s) < 1:
        return set()

    # Initialize result set
    cat = {0} # category 0 is always included

    # Test if all letters are consonants
    test = True
    for c in s:
        if c not in CONSONANTS:
            test = False
            break
    if test == True:
        cat.add(1)

    # Test if all letters are vowels
    test = True
    for c in s:
        if c not in VOWELS:
            test = False
            break
    if test == True:
        cat.add(2)

    # Test if the substring is a consonant/vowel pair
    if len(s) == 2:
        if s[0] in CONSONANTS and s[1] in VOWELS:
            cat.add(3)
        if s[0] in VOWELS and s[1] in CONSONANTS:
            cat.add(4)

    # Return the complete category set
    return cat

#==============================================================================

def _alternating(s, num=2):
    """_alternating(s[, num]) -> bool
    Determines whether a substring alternates between consonants and vowels.

    Positional arguments:
    s (str) -- string to categorize

    Keyword arguments:
    [num=2] (int) -- number of switches needed to constitute "alternating"

    Returns:
    (bool) -- True if the string switches back and forth between consonants and
              vowels more than once, and False otherwise
    """

    # Alternation requires at least 3 characters
    if len(s) < 3:
        return False

    # Go through each letter and count switches
    switches = 0 # number of consonant/vowel switches
    con = False # whether the current character is a consonant
    if s[0] in CONSONANTS:
        con = True
    for c in s[1:]:
        if (c in CONSONANTS) != con:
            con = not con
            switches += 1
        if switches >= num:
            return True

    # If too few switches were found, the string does not alternate
    return False

#==============================================================================

def pair_frequency(fin, fout, lb=None, ub=None):
    """pair_frequency(fin, fout[, lb][, ub])
    Generates a table of letter pair frequencies

    Positional arguments:
    fin (str) -- name of input word list file
    fout (str) -- name of output statistic file

    Keyword arguments:
    [lb=None] (int) -- lower bound letter index (None to start at beginning)
    [ub=None] (int) -- upper bound letter index (None to process until end)

    The input file should consist of a dictionary text file, with a single word
    on each line.

    The output is a tab-separated text file containing the frequencies of all
    possible letter pairs. Row i, column j indicates the letter pair ij.

    The optional bounds can be used to process only a limited range of the word
    list. Every list index in the interval [lb,ub) is included. Setting either
    to None causes that bound to be ignored.
    """

    # Start timer
    start = time.time()

    # Initialize a dictionary with every possible letter pair
    pairs = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        for j in alphabet:
            pairs[i+j] = 0
    
    # Read word list line-by-line and record statistics
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

            # Go through each letter pair
            for j in range(len(word)-1):
                pairs[word[j]+word[j+1]] += 1
    
    # Write word list to output file
    with open(fout, 'w') as f:
        for i in alphabet:
            line = "" # line of output table
            for j in alphabet:
                line += str(pairs[i+j])
                if j != 'z':
                    line += '\t'
            # Write line to file
            print(line, file=f)

    # Report total time
    print("Processed '" + fin + "' after " + str(time.time() - start) +
          " seconds.")

#==============================================================================

# Automatically process dwyl dictionary
if __name__ == "__main__":
    gather_stats("words_alpha.txt", "word_statistics.ini")
    pair_frequency("words_alpha.txt", "letter_pairs.txt")
