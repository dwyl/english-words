"""A script for gathering letter distribution statistics from a word list."""

import configparser

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

    # Define multidimensional array of statistic dictionaries
    stats = [[[{} for p in range(4)] for t in range(5)] for n in range(5)]

    # Define character arrays for use in naming the dictionaries
    dic_numbers = [str(i) for i in range(1, 6)]
    dic_types = ["_a", "_c", "_v", "_cv", "_vc"]
    dic_pos = ["_a", "_b", "_e", "_m"]
    
    # Define consonant and vowel lists
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    
    # Read word list line-by-line and record statistics
    with open(fin, 'r') as f:
        num = -1 # current word index
        for line in f:
            num += 1
            
            # Respect bounds
            if (lb != None) and (num < lb):
                continue
            if (ub != None) and (num >= ub):
                break

            # Get current word
            word = line.strip()

            # Process each character
            for c in word:
                # Singleton statistics
                pass

            ###
            print(str(num) + ": " + word)

    # Load statistic dictionaries into INI file parser
    config = configparser.ConfigParser()

    # Write INI file
    ###with open(fout, 'w') as f:
    ###    config.write(f)

    del config

# Automatically process dwyl dictionary
if __name__ == "__main__":
    gather_stats("words_alpha.txt", "word_statistics.ini", ub=10)
