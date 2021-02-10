"""A script for gathering letter distribution statistics from a word list.

The main public function, gather_stats(), can be used to gather letter
statistics for a given word list file and write the contents of the statistic
dictionaries to an INI file.

If run as a script, the default word list is the dwyl English word dictionary
"words_alpha.txt".
"""

import configparser

# Define global consonant and vowel lists
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"

#==============================================================================

def gather_stats(fin, fout, lb=None, ub=None):
    """gather_stats(fin, fout[, lb][, ub])
    Gathers letter statistics from a given file.

    Positional arguments:
    fin (str) -- name of input word list file
    fout (str) -- name of output statistic file

    Keyword arguments:
    [lb=None] (int) -- lower bound letter index (None to start at beginning)
    [ub=None] (int) -- upper bound letter index (None to process until end)

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
                    # Determine the types of letters
                    cat = _categorize(ss) # set of valid type indices
                    for t in cat:
                        # Log in dictionary depending on position
                        pass

            ###
            print(str(num) + ": " + word)

    # Load statistic dictionaries into INI file parser
    config = configparser.ConfigParser()

    # Write INI file
    ###with open(fout, 'w') as f:
    ###    config.write(f)

    del config

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

# Automatically process dwyl dictionary
if __name__ == "__main__":
    gather_stats("words_alpha.txt", "word_statistics.ini", lb=5, ub=6)
