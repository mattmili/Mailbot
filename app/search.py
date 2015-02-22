
from google.appengine.api import search

querystring = 'stories'
search(query)
doc_limit = 2

# a query string like this comes from the client
def search(query):
	
	try:
	  index = search.Index(INDEX_NAME)
	  search_query = search.Query(
	      query_string=querystring,
	      options=search.QueryOptions(
	          limit=doc_limit))
	  search_results = index.search(search_query)
	  print search_results
	except search.Error:
	  print 'error'
