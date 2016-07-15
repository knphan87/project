'''import xml.etree.ElementTree as ET
import urllib
total = 0
urllink = raw_input("Enter location: ")
print "Retrieving ",urllink
data = urllib.urlopen(urllink).read()
print 'Retrieved ',len(data)," characters"
tree = ET.fromstring(data)
counts = tree.findall("comments/comment/count")
print "Count: ",len(counts)
for count in counts:
    total += int(count.text)
print "Sum: ",total'''

import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'true', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
