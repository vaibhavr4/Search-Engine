import json

def dictread(filename):
   
    d={}
    d= json.load(open(filename))
    

    # for k,v in d.items():
        
    #     for k1, v1 in v.items():
    #         if k=="tropical":
    #             print("V:",k1)
    #unique_docs(d)
    return d

def unique_docs(d):
    uniqueDocuments=[]
    outputdocs=[]
    for k,v in d.items():
        for k1, v1 in v.items():
            uniqueDocuments.append(int(k1))
    temp=set(uniqueDocuments)
    uniqueDocuments=list(temp)
    uniqueDocuments.sort()
    for doc in uniqueDocuments:
        outputdocs.append(str(doc))
    #print(outputdocs)
    
    return outputdocs

