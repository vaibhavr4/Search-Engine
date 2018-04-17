import math 		# math module from python for log operation
import sys          # sys module for handling command line arguments passed to the module

# All locally defined modules with their imported functions

from queryProcessor import queryProcessor
from queryProcessor import queries
from docsread import dictread
from docsread import unique_docs

# calculating the value for K
def Kcalc(doclength):
	
	K = {}
	for document in uniqueDocuments:
		K[document] = k1*((1-b) + (b* doclength[document]/avgdoclength))
	print("K value:",K)
	return K

#calculating BM25 score for each query term
def BM25score(maximumResults):
	kValues = Kcalc(doclength)								# K value for each document in a Dictionary
	qid = -1
	i=0
	for query in querySet:
		qid += 1

		docWeights = {}
		for document in uniqueDocuments:
			
			documentScore = 0
			for queryTerm in list(set(queryTerms[query])):
				termWeight = query_term_weight (kValues[document], queryTerm, queryTerms[query], document)
				
				score = scoringFunction (document, queryTerm)
				
				if termWeight != 0: 
					documentScore += math.log(termWeight*score)
			docWeights[document] = documentScore
			print("QID:",qid+1,"DOCUMENT:",document)
			
		#print("QID:",qid,"COUNT DOCS:",i+1)

		

		rankedDocsFinal(docWeights, qid, maximumResults)	
	
# display the final maximumResults document
def rankedDocsFinal(docWeights, qid, maximumResults):
	system_name = "Vaibhav_BM25"
	sortedList = sorted(docWeights, key=docWeights.__getitem__)
	top = sortedList[-(maximumResults):]
	top.reverse()
	rank = 0
	for doc in top:
		rank += 1
		print (qid+1),"Q0"," ", doc," ",rank, " ", docWeights[doc], system_name
		with open("bm25_output.txt",'a') as out:
			out.write('%r\t%r\t%r\t%r\t%r\t%r\t\n' % (qid+1,"Q0",doc, rank, docWeights[doc], system_name))
	    		


#to calculate th equery term weight for each term in index
def query_term_weight(K, term, query, doc):
	#print("TERM:",term)
	temp=[]
	
	if term in index:
		termFrequency = 0
		docTuple = ()
		for k,v in index.items():
			for k1, v1 in v.items():
				#print("V1:",v1)
				if k==term:

					if k1== doc:
						docTuple = (doc, v1)
		
		if docTuple != ():
			termFrequency = int(docTuple[1])

		queryFrequency = int(query.count(term))
		
		query_term_weight = (termFrequency*queryFrequency*(1.2 +1)*(100 +1)) / ((K+termFrequency)*(100 +queryFrequency))
		return query_term_weight	

	else:
		return 0



def scoringFunction(doc, queryTerm):
	
	if queryTerm in index:
		relevant_docs = len(index[queryTerm])
		return (total_docs - relevant_docs + 0.5)/(relevant_docs + 0.5)
	else:
		return (total_docs + 0.5) / 0.5


# Main. The program starts from here
if __name__ == "__main__" :

	# Command line arguments all loaded into proper local variables
	indexFile = dictread("unigram_index_json.json")
	queryFile = "queries.txt"
	maximumResults = 100
	uniqueDocuments=[]


	# Constant parameters in the problem statement
	k1 = 1.2
	b = 0.75
	k2 = 100
	index = indexFile
	uniqueDocuments = unique_docs(index)						    # Set of Docs								
	total_docs = len(uniqueDocuments)								# Size of Corpus
	doclength = dictread("doc_length.txt")							# Size of each document in a Dictionary


	querySet = queries(queryFile)									# Set of Queries

	queryTerms = queryProcessor(querySet)							# Tokenised query terms in a Dictionary

	avgdoclength = sum(doclength.values())/total_docs	# Average document length

	BM25score(maximumResults)										# Function call which computes document score

