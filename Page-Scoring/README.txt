PAGE SCORING AND RANKING USING Lucene AND BM-25 model


FOLDERS:
Task1
Task2

Task1:
parsed_docs - This folder contains the parsed documents from Task1 of HW3
HW4.java - The java source code for scoring and retrieval using Lucene
Lucene_document_list - The output file for the Lucene code with the documents ranked.
query_file.txt - Contains the query submitted

Procedure to run for Task1:
---Using Lucene version 7.1.0---
javac HW4.java
java HW4
 When prompted;
 Enter the FULL path where the index will be created: (e.g. /Usr/index or c:\temp\index)
 **Enter the path where the output file should be located**
 When prompted;
 Enter the FULL path to add into the index (q=quit): (e.g. /home/mydir/docs or c:\Users\mydir\docs)
[Acceptable file types: .xml, .html, .html, .txt]
 ** Enter the path of parsed_docs folder **
 ** Enter "q" to quit **
 
 
Task2:
bm25_output.txt - The output of ranked documents based on BM25
bm25_scoring.py - The source code of bm25 ranking
doc_length.txt - The file output from HW3-Task2 which contains the length of each document parsed.
docsread.py - Used to read the input file and convert it into a data structure usable in python
queries.txt - Contains the list of queries submitted
queryProcessor.py - Used to parse the queries into a data structure
unigram_index_json.json - The unigram index file generated in HW3-Task2 which can be transformed to a dictionary data structure

Procedure to run for Task2:
python bm25_scoring.py

***************************************************************************************************************************************
*******Documents are renamed to avoid duplicates or overlap*********************
Please find the name mapping to documents in "File_name_mapping.txt" file.

Top_5_ranked_docs - This contains the top 5 ranked documents and scores from both Lucene and BM25.
Comparison of results.docx - The comparison of top 5 rannked results of both models are compared