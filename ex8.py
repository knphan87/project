import urllib
import json

serviceurl  = 'http://python-data.dr-chuck.net/geojson?'
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1:break
    url = serviceurl + urllib.urlencode({'sensor':'false','address':address})
    print 'Retrieving ',url
    urldata = (urllib.urlopen(url)).read()
    print urldata

    print "Retrieved ",len(urldata)," characters"

    try: js = json.loads(str(urldata))
    except: js = None

    if 'status' not in js or js['status'] !='OK':
        print '==== Failure To Retrieve ===='
        print urldata
        continue

    place_id = js['results'][0]['place_id']
    print "Place id ",place_id
