import json
import urllib

total = 0
urlinput = raw_input("Enter location: ")

print "Retrieving ",urlinput
urllink = urllib.urlopen(urlinput)
datainput = urllink.read()

info = json.loads(datainput)
print 'Retrieved ', len(datainput), " characters"

for item in info["comments"]:
    total = total + item["count"]
print "Count: ",len(info["comments"])
print "Sum: ",total
