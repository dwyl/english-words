# List Of English Words

This is a fork of the [dwyl](https://github.com/dwyl) [List of English Words](https://github.com/dwyl/english-words) repo, to be used for gathering English letter distribution statistics. I've edited down the contents of the repo to include only the files I need and added some Python scripts for gathering statistics, primarily as part of the setup for my [Slight Misspeller](https://github.com/adam-rumpf/slight-misspeller) project. The authors' original [(un)license](https://github.com/dwyl/english-words/blob/master/LICENSE.md) remains intact.

See the original README below.

> A text file containing over 466k English words.
> 
> While searching for a list of english words (for an auto-complete tutorial)
> I found: http://stackoverflow.com/questions/2213607/how-to-get-english-language-word-database which refers to [http://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable](https://web.archive.org/web/20131118073324/http://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable) (archived).
> 
> No idea why infochimps put the word list inside an excel (.xls) file.
> 
> I pulled out the words into a simple new-line-delimited text file.
> Which is more useful when building apps or importing into databases etc.
> 
> Copyright still belongs to them.
> 
> Files you may be interested in:
> 
> -  [words.txt](https://github.com/dwyl/english-words/blob/master/words.txt) contains all words.
> -  [words_alpha.txt](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) contains only [[:alpha:]] words (words that only have letters, no numbers or symbols). If you want a quick solution choose this.
> -  [words_dictionary.json](https://github.com/dwyl/english-words/blob/master/words_dictionary.json) contains all the words from words_alpha.txt as json format. 
> If you are using Python, you can easily load this file and use it as a dictionary for faster performance. All the words are assigned with 1 in the dictionary.
> See [read_english_dictionary.py](https://github.com/dwyl/english-words/blob/master/read_english_dictionary.py) for example usage.
