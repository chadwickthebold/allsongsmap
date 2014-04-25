import requests
import time
import sqlite3
import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime

def unix_time(dt):
	epoch = datetime.utcfromtimestamp(0)
	delta = dt - epoch
	return delta.total_seconds()

def hash_name(name):
	hashStr = hashlib.sha256(name).hexdigest()
	hashNum = int(hashStr,base=16)
	return hashNum

# Open the log file and print the starting time
log = open('allsongsmap.log','w')
startTime = time.localtime()
startTimeString = time.strftime('%a, %d-%m-%y %H:%M %p', startTime)
log.write('Started allsongsmap at : ' + startTimeString + '\n')

# Parse the file containing API keys
keyFile = open('keys.prop','r')
H = dict(line.strip().split('=') for line in keyFile)
keyFile.close

# Placeholder variables
date = ''
dateFormat = '%a, %d %b %Y'
numResults = 20
numArtistTotal = 0
artistId = 0

# Open the sqlite database connection
conn = sqlite3.connect('allsongsmap.db')
c = conn.cursor()

# Create the Story table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS Stories(storyid integer, date text)''')

# Create the Artist table "
c.execute('''CREATE TABLE IF NOT EXISTS Artists(artistid text, artistname text)''')

# Create the Artistmap table "
c.execute('''CREATE TABLE IF NOT EXISTS Artistmap(storyid integer, artistid text)''')

#TODO add checking for existing values
#TODO add verbose output option

while (numResults >= 20):
	# Get the start time of the request
	start = time.time()

	# Per-request placeholder variables
	# These must be reset at the beginning of each request
	numArtist = 0
	numResults = 0
	resString = ''
	executeString = ''
	artistExecString = ''

	# Make the NPR API request
	log.write('Making NPR request with date = ' + date + '\n')
	r = requests.get("http://api.npr.org/query?", params={'id':'15709577','apiKey':H["NPR"],'fields':'song,storyDate','output':'NPRML','endDate':date,'numResults':'20'})	
	log.write('Returned Status Code : ' + str(r.status_code) + '\n')
	nprml = ET.fromstring(r.text.encode('utf-8'))

	# Iterate over all the returned elements from the request
	innerList = nprml[0]
	for child in innerList:
		numResults += 1
		if (child.tag == 'story'):
			# Record the important details about the current story
			story = child
			storyId = story.attrib['id']
			dateString = story.find('storyDate').text[:-14].strip()
			dateObj = datetime.strptime(dateString, dateFormat)
			dateNum = str(unix_time(dateObj))
			date = str(dateObj.year)+'-'+str(dateObj.month)+'-'+str(dateObj.day)
			resString = storyId + ' : ' + date + ' : ' + dateNum 
			
			# Iterate over all the songs found in the current story
			#TODO check if artist has already been inserted into the Artists table
			#TODO create artistmap table
			for song in story.findall('song'):
				songArtist = song.find('artist').text
				album = song.find('album')
				albumArtist = album.find('albumArtist').text
				
				# Encode the song artist and album artist
				if (songArtist):
					songArtist = songArtist.encode('utf-8')
				if (albumArtist):
					albumArtist = albumArtist.encode('utf-8')

				# If a song artist exists, record its necessary details
				if (songArtist and (songArtist != 'Untitled')):
					numArtist += 1
					artistId = str(hash_name(songArtist))
					resString = resString + ',' + songArtist
					artistExecString = "INSERT INTO Artists VALUES ('" + artistId + "','" + songArtist.replace("'","''") + "')"
					log.write('Executing: ' + artistExecString + '\n')
					c.execute(artistExecString)
					artistmapExecString = 'INSERT INTO Artistmap VALUES (' + storyId + ",'" + artistId + "')"
					log.write('Executing: ' + artistmapExecString + '\n')
					c.execute(artistmapExecString)

				# If an album artist exists and is not the same as the song artist, record its necessary details
				if (albumArtist and (songArtist != albumArtist) and (albumArtist != 'Untitled')):
					numArtist += 1
					artistId = str(hash_name(albumArtist))
					resString = resString + ',' + albumArtist
					artistExecString = "INSERT INTO Artists VALUES ('" + artistId + "','" + albumArtist.replace("'","''") + "')"
					log.write('Executing: ' + artistExecString + '\n')
					c.execute(artistExecString)
					artistmapExecString = 'INSERT INTO Artistmap VALUES (' + storyId + ",'" + artistId + "')"
					log.write('Executing: ' + artistmapExecString + '\n')
					c.execute(artistmapExecString)
			
			# If artists were found in this story, insert the story into the Stories table
			if (numArtist > 0):
				artistString = artistString.replace("'","''")
				executeString = 'INSERT INTO Stories VALUES (' + storyId + "," + dateNum + ")"
				log.write(resString + '\n')
				log.write('Executing : ' + executeString + '\n')
				c.execute(executeString)
				numArtistTotal += numArtist
			
			numArtist = 0
			artistString = ''
			resString = ''
			executeString = ''
	
	# Get the ending time of the request
	end = time.time()
	diff = end - start
	log.write('finished call and conversion in ' + str(diff) + ' seconds\n')

	# Rate-limit the NPR API call to 1 per 5 seconds
	remain = start + 5 - end
	if remain > 0:
		time.sleep(remain)

endTime = time.localtime()
endTimeString = time.strftime('%a, %d-%m-%y %H:%M %p',endTime)

# Commit DB changes and close connection
conn.commit()
conn.close()

# Finish and close the log
log.write('Found ' + str(numArtistTotal) + ' Artists')
log.write('Finished allsongsmap at ' + endTimeString +' \n')
log.close()
