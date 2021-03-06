#!/usr/bin/python

import sys

word2count = {}

for line in sys.stdin:
	line = line.strip()

	word,count = line.split('\t',1)
	
	try:
		count = int(count)
	except:
		continue

	try:
		word2count[word] = word2count[word] + count
	except:
		word2count[word] = count

for word in word2count.keys():
	count = word2count[word]
	if count > 1:
		print '%s\t%s' % (word, count)
