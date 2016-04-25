

# prints all the information of the user including the latitude and location
# need to change the information into a csv file to retrieve the latitude and location

from lxml import etree
import urllib

# webPage will receive information from the url
webPage = urllib.urlopen("https://api.instagram.com/v1/users/186357295/media/recent/?access_token=186357295.1677ed0.6ce9f99b45fc4ecfb460fd12acc0653f")

#pageinfo will hold all the data displayed on the screen with the latitude and longitude
pageInfo = webPage.read()

#print pageInfo


#--------------------Finds latitude


# finds the latitude index
latitudeIndex = pageInfo.find("latitude")
latitudeIndex = latitudeIndex + 10

# retrieve the latitude
latitudeString = ""

# loop will retrieve and add the latitude location as a string to the variable latitudeString
while (pageInfo[latitudeIndex] != ','):

		latitudeString += pageInfo[latitudeIndex]
		latitudeIndex = latitudeIndex + 1

# convert latitude variable string to a float
latitudeLocation = float(latitudeString)

print "Latitude: ", latitudeLocation
	

#--------------------finds longitude

# finds the longitude index
longitudeIndex = pageInfo.find("longitude")
longitudeIndex = longitudeIndex + 11

# retrieve the longitude
longitudeString = ""

# loop will retrieve and add the longitude location as a string to the variable longitudeString
while (pageInfo[longitudeIndex] != ','):

		longitudeString += pageInfo[longitudeIndex]
		longitudeIndex = longitudeIndex + 1

# convert latitude variable string to a float
longitudeLocation = float(longitudeString)

print "Longitude: ", longitudeLocation


#----------------------------display location on web browser


import webbrowser


# html file 
f = open('pinDrop')


# location of html file
filename = '/home/diegomedina/SchoolWork/CSUMB - Multimedia/instagramAPI/' + 'pinDrop.html'
webbrowser.open_new_tab(filename)












