from stemming.porter2 import stem
import sys
import re

for line in sys.stdin:
	line = line.strip()

	words = line.split(",") 
	if re.match('\d\d/\d\d/\d{4}', words[0]):
		line = ','.join(words[4:])
		line = re.sub(r'\W+', ' ', line)
		line = re.sub(r" +", ' ', line)
		words = line.split()
		for word in words:
			print '%s\t%s' % (word.lower(), "1")

