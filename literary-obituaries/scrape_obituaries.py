#!/usr/bin/python

"""
Scrapes the Telegraph obituary pages and outputs to stdout a csv in the format:

date,publisher,type,name,content,category
...

"""
import urllib
import sys

# http://docs.python-requests.org/en/latest/
import requests

# http://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup as Soup

# http://code.google.com/p/soupselect/
from soupselect import select

# http://code.google.com/p/parsedatetime/
import parsedatetime as pdt


def parse_obituary(url,category):
	"""
	Extracts the necessary information from a single obituary page
	"""
	page = requests.get(url)
	soup = Soup(page.text)
	try:
		date = select(soup, 'p strong')[0].contents[0]
		date = date[date.rfind('died ')+5:].strip()
		cal = pdt.Calendar()
		print >> sys.stderr, 'parsing',date
		date = cal.parseDateText(date)
	except:
		print >> sys.stderr, 'failed to parse'
		return
	date = str('%s/%s/%s' % (date[2],date[1],date[0]))
	publisher = 'Telegraph'
	type = 'obituaries'
	name = select(soup, '.storyHead h1')[0].contents[0]
	content = ''
	for para in select(soup, '#mainBodyArea p'):
		if len(para.contents) > 0:
			content = content + para.contents[0]

	content = content.strip().replace('"','\'')		
	content = content.strip().replace('\n','')
	
	print >> sys.stdout, '%s,%s,%s,%s,"%s","%s"' % (date.encode("UTF-8"),
													publisher.encode("UTF-8"),
													type.encode("UTF-8"),
													name.encode("UTF-8"),
													content.encode("UTF-8"),
													category.encode("UTF-8"))



# Main function to grab the individual pages from the telegraph page

r = requests.get('http://www.telegraph.co.uk/news/obituaries')

soup = Soup(r.text)
for i in select(soup, '.secRelSections h3 a'):
	section_url = i['href']
	print >> sys.stderr, i.contents[0]

	sec = requests.get(section_url)
	soup = Soup(sec.text)
	
	for summ in select(soup, '.oneHalf .summary h3 a'):
		url = 'http://www.telegraph.co.uk/'+summ['href']
		print url
		parse_obituary(url,i.contents[0])

