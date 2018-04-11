import os
import operator

CURRENT=os.getcwd()

# Folder to read the parsed articles
FOLDER= os.path.join(CURRENT,'Task1')

# Used to generate index for n grams
def generate_ngram(n):
    
    inverted_index = {}
    doc_tokens = {}
    files = [f for f in os.listdir(FOLDER) if f.endswith(".txt")]
    print("Total Documents:",len(files))
    counter=0

    for f in files:
    	
    	# get file name alone without extension
    	doc_id= files[counter][:-4]
    	print("FILE_NAME:",doc_id)

    	doc= open(os.path.join(FOLDER,f), 'r').read()
    	# update doc_tokens which contains the number of tokens in each doc
    	doc_tokens.update({f:len(doc.split())})
    	print("Doc:",f,"No, of tokens:",len(doc.split()))
    	# for each term in document
    	token_list = doc.split()
    	# for value of n between 1 to 3, generate n gram index
    	for i in range(len(token_list)-n+1):
    		if n==2:
    			term = token_list[i]+" "+token_list[i+1]
    		elif n==3:
    			term = token_list[i]+" "+token_list[i+1]+" "+token_list[i+2]
    		else:
    			term= token_list[i]
    		# if term not already in index, add the term and document id
    		if term not in inverted_index.keys():
    			doc_dict ={doc_id:1}
    			inverted_index.update({term:doc_dict})
    		# if term available in index, add the document id to that term
    		elif doc_id not in inverted_index[term].keys():
    			inverted_index[term].update({doc_id:1})
    		# if both term and document id is present update the term frequency count
    		#      of that particular document
    		else:
    			inverted_index[term][doc_id] += 1
    
    	counter+=1
    print("INVERTED INDEX:",inverted_index)
    # writing inverted index to file
    file_name= "INVERTED_INDEX"+str(n)+"GRAM.txt"
    for k,v in inverted_index.items():
    
        print('Inverted Index',k,':',v,'\n')
        with open(file_name,'a') as out_link:
            out_link.write('{0}:{1}\n'.format(k, v))
            out_link.close()
    # function call for generating term and document frequency tables
    table_gen(inverted_index,n)
	
	
# function for generating term and document frequency tables
def table_gen(inverted_index,n):
    
    term_freq={}
    doc_freq={}
    for term in inverted_index:
    	freq=0
    	doc_list =[]
    	for doc_id in inverted_index[term].keys():
    		doc_list.append(doc_id)
    		freq += inverted_index[term][doc_id]
    	term_freq.update({term:freq})
    	doc_freq.update({term:doc_list})
    # sort terms based on descending order of term frequencies
    sorted_term_freq = sorted(term_freq.items(), key=operator.itemgetter(1), reverse=True)
    term_freq_table_gen(sorted_term_freq,n)
    # sort document id's in lexographical order
    sorted_doc_freq = sorted(doc_freq.items(), key=operator.itemgetter(0))
    doc_freq_table_gen(sorted_doc_freq,n)
        
# for generating term frequency tables for ngram       
def term_freq_table_gen(sorted_term_freq,n):
	out_file  = open(str(n) +"-GRAM_TERM_FREQ.txt",'w')
	for token in sorted_term_freq:
		out_file.write(str(token[0])+ ":" + str(token[1]) + "\n")
	out_file.close()
    
    
 # for generating document frequency tables for ngram
def doc_freq_table_gen(sorted_doc_freq,n):
	out_file  = open(str(n) +"-GRAM_DOC_FREQ.txt",'w')
	for token in sorted_doc_freq:
		out_file.write(str(token[0])+ " " +str(token[1]) + " " + str(len(token[1])) + "\n")
	out_file.close()
    
# get input for n-gram 
try:
    user_input = int(input("Input value for ngram from below:\n1\n2\n3\n")) 
    if not user_input:
        raise ValueError('Invalid value')
    elif user_input not in(1,2,3):
    	raise ValueError('Enter from options provided')
    else:
    	generate_ngram(user_input)
except ValueError as e:
    print(e)   
   


		
		

	

	
	
	
