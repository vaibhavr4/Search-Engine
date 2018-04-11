from urllib.request import urlopen as uReq
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re 
import string 


##########file creation for each article############
def file_create(url,filename):
		
	html = uReq(url)
	soup= BeautifulSoup(html,'lxml')
    
    # remove all javascript and stylesheet code
	for script in soup(["script", "style","semantics","dl"]): 
		script.extract()
	    
	title_text = soup.find('title').get_text()
	
	# removing images, tables, references and unwanted parts of article
	content= soup.findAll('p')
	s=''
	for p in content:
		s=s+" "+p.get_text()
	
	content = soup.find("div", {"id":"mw-content-text"}).get_text()
	reference= soup.find("div",{"class":"reflist columns references-column-width"})
	if reference:
		content=content.replace(reference.get_text(),' ')
		
	
	image= soup.find("div",{"class":"thumb tright"})
	if image:
		content=content.replace(image.get_text(),' ')
	
	table= soup.find("table",{"class":"wikitable"})
	if table:
		content=content.replace(table.get_text(),' ')
	
	toc= soup.find("div",{"id":"toc"})
	if toc:
		content=content.replace(toc.get_text(),' ')

	edit= soup.find("span",{"class":"mw-editsection"})
	if edit:
		content=content.replace(edit.get_text(),' ')
	

	all_text = title_text+ content

	  
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in all_text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	all_text = '\n'.join(chunk for chunk in chunks if chunk)
	
	clean_text= cleanInput(all_text)
		
	file= str(filename)+".txt"
	with open(file,'w') as out_link:

	# writing links to file
		out_link.write(str(clean_text))
		out_link.close

##########################################################################################

# parsing for punctuation

def cleanInput(input):
	    
	input = re.sub('\n+', " ", input)        
	input = re.sub(' +', " ", input)
	input= re.sub(r"(?<!\d)[.,;:](?!\d)"," ",input,0)
	input= re.sub(r"(?<![a-zA-Z\d])[-](?!\[a-zAa-Z\d)"," ",input,0)
	input=' '.join(word.strip(string.punctuation) for word in input.split())
	input= re.sub(r'\[.*?\]'," ",input)
	input= re.sub(r"([~|!/&$#'\"()\[\]=?\\])"," ",input,0)
	input = bytes(input, "UTF-8")    
	input = input.decode("ascii", "ignore")    
	   
	return input.lower()



#########retrieving files from file#############

def articlegen():
	
	graph_file = open('BFS_LINKS_BASED_GRAPH.txt', 'r') 
	line_file = graph_file.read().splitlines()
	count=1
	dict={}
	for line in line_file:
	    line = line
	    split=line.split('/wiki/')
	    filename= split[1]
	    dict={count:filename}
	    print("DICT:",dict)
	    # writing file_name mapping to file
	    with open("File_name_mapping.txt",'a') as out:
	    	out.write(str(dict))
	    	out.write("\n")
	    	out.close

	
			
			
	    file_create(line,count)

	    count+=1

################### function call #################################	
articlegen()