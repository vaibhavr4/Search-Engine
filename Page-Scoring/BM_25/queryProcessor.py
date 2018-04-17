

def queries(fileName):
	f = open(fileName,'r')

	queryList = []
	for line in f:

		if line[-1] == '\n':				# Remove new line character
			queryList.append(line[0:-1])
		else:
			queryList.append(line)
	print("QUERY LIST:",queryList)
	queryProcessor(queryList)
	return queryList


def queryProcessor(querySet):
	
	queryTerms = {}

	for query in querySet:
		queryTerms[query] = query.split(" ")
	print("QUERY TERM:",queryTerms)
	return queryTerms





