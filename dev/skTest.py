import requests
import xml.etree.ElementTree as ET

# Parse the file containing API keys
keyFile = open('keys.prop','r')
H = dict(line.strip().split('=') for line in keyFile)
keyFile.close

#mbid to test - speedy ortiz @ Great Scott on Dec. 19
mbid = "4fbf1a3d-a649-4f8e-9ddf-347f6ba2d307"
name="speedy+ortiz"

# Get Boston location ID, search by name
r = requests.get("http://api.songkick.com/api/3.0/search/locations.xml?", params={'query':'Boston','apikey':H["SONGKICK"]})
resultsPage = ET.fromstring(r.text.encode('utf-8'))
results = resultsPage[0]
location = results[0]
metroArea = location.find("metroArea")
metroId = metroArea.attrib['id']

# make request with mbid and location
r = requests.get("http://api.songkick.com/api/3.0/events.xml?", params={'location':'sk:'+metroId,'artist_name':name,'apikey':H["SONGKICK"]})