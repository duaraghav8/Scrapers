import httplib2;
from bs4 import BeautifulSoup as Soup;

def extract_content (counter, html):
	soup = Soup (html);
	div = soup.find ('div', {'class':'article-content'})
	f = open (str (counter) + '.txt', 'w');
	f.write (div.text);
	f.close ();

uri = 'http://www.psexam.com/Multiple-Choice-Questions-MCQs-from-C++/basics-of-c-objective-questions-mcqs-set-####.html';
counter = 1;

for current_page in range (1, 9):
	current_uri = uri.replace ('####', str (current_page));
	http = httplib2.Http ();
	print ('fetching:\t %s' %(current_uri));
	head, html = http.request (current_uri);
	extract_content (counter, html.decode ());
	counter += 1;
