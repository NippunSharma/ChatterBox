"""Google search for stackoverflow"""

from googlesearch import search  

def google_search(query):
    query+=" site:stackoverflow.com"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        print(j) 
