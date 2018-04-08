#importing required libraries

from urllib.request import urlopen as uReq
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from time import sleep
from time import time
from random import randint
import re 


#initializing seed value
seed = "/wiki/Tropical_cyclone"

# initializing empty list and appending the seed url to it
main_list = []
keyword=""

 
 
def link_list_generator (url,keyword):
	
#getting the url and soup
	
	
	html= uReq("http://en.wikipedia.org"+url)
	bs= BeautifulSoup(html,'lxml')

#one second delay in requests
	sleep(1)
# to retrieve links and using regex to limit the links to crawl
	links = bs.find("div",{"id" : "bodyContent"}).findAll("a" , href=re.compile("^((\/wiki\/)(([a-zA-Z]+)([_\-\$]+))*(rain)(.)*)", re.IGNORECASE))
	temp_list = []
	
# generate_list links crawled
	for link in links:
			newPage=link['href']
			if newPage not in temp_list:
				temp_list.append(newPage)
	
	print(temp_list)
	return temp_list
	 
# =================== end of function link_list_generator =====================
 
def web_crawl(seed,keyword):
#setting initial values for variables
	level_set_size = 1
	current_index = 0
	to_crawl=100
	current_depth=1
	max_depth=6
	temp_list_of_links=[]
	main_list=[seed]
	print("Key....",keyword)
	
# checking for end conditions 
	while current_index < len(main_list):
 
		if current_index >= to_crawl:
			return 0;
		if current_depth >  max_depth:
			return 0;

# decrement level_set_size , denotes the end of a level of crawl			
		level_set_size -=1;
 
 
# calling link_list_generator function for each element of list		
		temp_list_of_links = link_list_generator(main_list[current_index],keyword);
		
#appending the list returned from function to existing list to carry out breadth first search
		for temp_link in temp_list_of_links:
			if temp_link not in main_list:
				main_list.append(temp_link);
		
 
#resetting values  of variables
		print("Level set size:",level_set_size)
		if level_set_size == 0:
			level_set_size = len(temp_list_of_links)
			print("Level set size:",level_set_size)
			temp_set_size = 0
			current_depth+=1
	 
		current_index+=1;

#writing to file
		
		with open('wiki_links_2.txt','a') as out_link:

# writing links to file
			
			out_link.write("http://en.wikipedia.org"+main_list[current_index] +"\n")
			out_link.close
		
		print("Depth:........",current_depth)
		print("Link crawled........",main_list[current_index])
		print("Number of links crawled:", current_index)
 
 
 
#============================FUNCTION CALL====================================== 
keyword=input("Please enter the keyword:")
print("The seed URL is:",seed)
web_crawl(seed,keyword)