import urllib
from bs4 import BeautifulSoup

count = 0
sum = 0
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs
    count = count + 1
    sum = sum + (int)(tag.contents[0])
print "Count ",count
print "Sum ",sum
