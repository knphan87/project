import urllib
from bs4 import BeautifulSoup

tagList = list()
urlList = list()
url = raw_input('Enter - ')
if (len(url) < 1):
    url = "http://python-data.dr-chuck.net/known_by_Braden.html"
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: ")) - 1
urlList.append(url)
print "Retrieving: ",urlList[0]

for i in range(count):

    html = urllib.urlopen(urlList[0]).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    tagList = list()
    for tag in tags:
        tagList.append(tag)
    url = tagList[position].get("href",None)
    print "Retrieving: ",url
    urlList.append(url)
