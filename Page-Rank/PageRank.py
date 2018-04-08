# importing required libraries
from math import log
import operator
from collections import defaultdict

#--------------FILE READ SECTION------------
graph_file = open('dfs_final_graph.txt', 'r') 
line_file = graph_file.read().splitlines()

#-------------------------------------------

P = []
# S is the set of sink nodes ,i.e. pages that have no outlinks
S = []
# M(p) is the set of pages that link to page p
M = {}
# L(q) is the number of outlinks from page q
L = {}
#d is the PageRank damping/teleportation factor
d = 0.85

PR = {}
newPR = {}
perplexity = []
sortPR = []

# temp_key=[]
# temp_val=[]

# Retrieving each key and inlinks from file
# Storing the page and inlinks as key value pair in dictionary M
# Storing the list of pages in P
for line in line_file:
    line = line.split(':')
    inlinks=line[1].split(' ')
    #outlinks.pop(-1)
    M[line[0]] = inlinks
    P.append(line[0])


# to find top 10 pages with max inlinks
# for key,value in M.items():
#     temp_key.append(key)
#     temp_val.append(len(value))
    
# temp_dict=dict(zip(temp_key,temp_val))

# sortedinlinks = sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True)
# print('Sorted top 10 based on inlinks:')
# for i in range(10):   
#     print ('\n',sortedinlinks[i])


#to find the pages that have no inlink
#for key,value in M.items():
#    if value==['']:
#        print('NO INLINK:',key)


#Initialize the number of outlinks for all pages to 0.
for i in P:
    L[i] = 0

#Storing the dict.values() of M in a list
M_values=list(M.values())

# for each value in list of values of dictionary M, update the number of outlinks L
for values in M_values:
    for value in values:
        if (value==''):
            L[value]=0
    
        L[value] += 1

#Populating the Sink node list S, i.e.pages that have no outlinks
for page in L.keys():
    if L[page] == 0:
        S.append(page)

# print sink links
#for a in S:
#    print('SINK LINKS:',a)
# N is the total number of pages.
N = len(P)


# Page Rank Implementation
def pagerank():
    for p in P:
        PR[p] = 1.0/N
    temp = 0
    # to check for convergence, calling is_convergence() function
    while not is_convergence(temp):
        #print (temp+1, is_convergence(temp))             
        sinkPR = 0
        for p in S:
            sinkPR += PR[p]
        for p in P:
            newPR[p] = (1.0 - d)/N
            newPR[p] += d*sinkPR/N
            for q in M[p]:
                if q=='':
                   continue
                newPR[p] += d*PR[q]/L[q]
        for p in P:
            PR[p] = newPR[p]
        temp += 1
    # Printing and writing the Pank rank of all pages to file
    for k,v in PR.items():
        print('Page_Rank of',k,':',v,'\n')
        with open('Page_rank_dfs.txt','a') as out_link:
            out_link.write('Page Rank of {0}:{1}\n'.format(k, v))
            out_link.close()
    # Calling sortfunc to sort pages according to page rank and display
    sortfunc(PR)

# Calculate perplexity value to check for convergence
# Perplexity is 2 raised to Shanon entropy of Page Rank distribution
def calc_perplexity():
    H = 0
    #print('PERPLEXITY---------')
    for p in PR.keys():
        H += - PR[p]*log(PR[p],2)
    #print(2**H)
    with open('Perplexity_dfs.txt','a') as outper:
        
        outper.write('\n')
        outper.write(str(2**H))
    return 2**H

# Function to check for convergence
# Page Rank can be considered as converged if the change in perplexity is 
#           less than 1 for at least 4 consecutive iterations
def is_convergence(j):
    perplexvalue = calc_perplexity()           
    perplexity.append(perplexvalue)
      
    if (len(perplexity)>=4):             
        if(abs(perplexity[j]-perplexity[j-1])<1 and abs(perplexity[j-1]-perplexity[j-2])<1 and 
            abs(perplexity[j-2]-perplexity[j-3])<1 and abs(perplexity[j-3]-perplexity[j-4])<1):
            return True
        else:
            return False
    else:
        return False

# Function definition to sort the page according to page rank and return top 50 links
def sortfunc(PR):
    # Sort the values in PR based on the rank of the page
    sortPR = sorted(PR.items(), key=operator.itemgetter(1), reverse=True)
    #print(sortPR)
    # Writing top 50 pages according to page rank to file
    with open('Page_rank_dfs_top_50.txt','a') as out:
        out.write('Page rank of top 50 DFS links:')
        out.write('\n')
        for i in range(50):   
            #print (sortPR[i])
        
            out.write('{0}\n'.format(sortPR[i]))
        out.close()



#-----------------FUNCTION CALL----------------------------
pagerank()