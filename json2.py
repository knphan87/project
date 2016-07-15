import json
import urllib

total = 0
urlinput = raw_input("Enter location: ")
print "Retrieving ",urlinput
urllink = urllib.urlopen(urlinput)
datainput = urllink.read()

info = json.loads(datainput)
print 'Retrieved ', len(info)

for item in info:
    total += item[comments][count]
print "Sum: ",total
