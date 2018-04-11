INVERTED INDEX with N-GRAM TERM AND DOCUMENT FREQUENCY

Installation:
1. Python version 3 and above
2. Install beautifulsoup
Procedure to run:
python <filename>.py

DESIGN APPROCH FOLLOWED:
------------------------------------------------------------------------------------------------
Task1:
-------------------------
In Task1 the parsing is done while downloading the articles.
This can be integrated with web crawling of HW1 so that directly the parsed
documents can be downloaded.
Also the documents are renamed to not contain duplicates and a seperate mapping of 
file names to document ID is done and stored.

Task2 & Task3:
--------------------------
Both Task2 and Task3 are integrated in the same code.
A function generate_ngram is defined to generate an index of n grams which is 1,2 or 3 here.
The output will be of the format; => Term:{DocID:TermFreq}       Eg: libration:{'995': 7}

For each n-gram index, the term and document frequencies are generated.

Term frequency format:
---------------------------
Term: term freq
Eg=> the:75125

Document frequency format:
---------------------------
Term [DocID] DocumentFreq
Eg. => fim ['258', '279'] 2

Files Generated:
---------------------------
1-GRAM_DOC_FREQ - Represents the document frequency list generated for 1 gram.
1-GRAM_TERM_FREQ - Represents the term frequency list generated for 1 gram.
2-GRAM_DOC_FREQ - Represents the document frequency list generated for 2 gram.
2-GRAM_TERM_FREQ - Represents the term frequency list generated for 2 gram.
3-GRAM_DOC_FREQ - Represents the document frequency list generated for 3 gram.
3-GRAM_TERM_FREQ - Represents the term frequency list generated for 3 gram.
INVERTED_INDEX1GRAM- Represents the Inverted Index generated for 1 gram.
INVERTED_INDEX2GRAM- Represents the Inverted Index generated for 2 gram.
INVERTED_INDEX3GRAM- Represents the Inverted Index generated for 3 gram.
File_name_mapping - Represents the file name mapping to document ID to avoid duplicates.
BFS_LINKS_BASED_GRAPH - Consists of the list of links crawled through BFS

Folder- Task1
Consists of the 1000 articles generated after parsing.

Python Source code:
---------------------------
Task_1.py - For parsing and generating files for 1000 articles crawled
Task_2_3.py - For generating n-gram inverted index, n-gram term and document frequency.

