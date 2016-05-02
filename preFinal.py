# (33 Latest pictures)

# prints all the information of the user including the latitude and location.
# need to change the information into a csv file to retrieve the latitude and location.

from lxml import etree
import urllib


#--------------------------------------------------retrieving user information---------------------------------------------------

# user information to look up.
userId = "186357295"

# instagram api url to retrieve user picture information.
url = "https://api.instagram.com/v1/users//media/recent/?access_token=186357295.1677ed0.6ce9f99b45fc4ecfb460fd12acc0653f&count=33"

# insterts user id in url.
userIdIndex = url.find("users/") + 6
instagramUserURL = url[:userIdIndex] + userId + url[userIdIndex:]



# webPage variable will hold the information from the url.
webPage = urllib.urlopen(instagramUserURL)

# pageinfo will hold all the data displayed on the screen with the latitude and longitude.
pageInfo = webPage.read()


# (next comment is only used for debugging - "print pageInfo").
#print pageInfo


# string for entire list of coordinates.
coordinatesString = " ["

# counter variable used to find every latitude and longitude within the url data without repeating any.
counter = 0

#--------------------------------------------------retrieves max_id--------------------------------------------------------------

maxIdIndex = pageInfo.find("max_id=") + 7
maxID = ""

while(pageInfo[maxIdIndex] != '"'):
	maxID += pageInfo[maxIdIndex]
	maxIdIndex = maxIdIndex + 1

#print maxID


#--------------------------------------------------------Finds coordinates (LOOP)-------------------------------------------------


while (pageInfo.find("max_id=") > 0):


	# loops through all the data until all the coordinates are found
	# " > 0 " so it does not become an infinite loop 
	while (pageInfo.find("latitude", counter) > 0 ):


		#-------------------------------------------------------finds latitude

		# finds the latitude index
		latitudeIndex = pageInfo.find("latitude", counter)
		latitudeIndex = latitudeIndex + 10

		# will make the next search continue where the last one was found
		counter = latitudeIndex

	
		# empty string to add the latitude into type string
		latitudeString = "["

		# loop will retrieve and add the latitude location as a string to the variable latitudeString
		while (pageInfo[latitudeIndex] != ','):
	
				latitudeString += pageInfo[latitudeIndex]
				latitudeIndex = latitudeIndex + 1
		
		latitudeString += ","
	
		coordinatesString += latitudeString
	
	
		#-------------------------------------------------------finds longitude

		# finds the longitude index
		longitudeIndex = pageInfo.find("longitude", counter)
		longitudeIndex = longitudeIndex + 11

		# empty longitude to add the longitude of type string
		longitudeString = ""

		# loop will retrieve and add the longitude location as a string to the variable longitudeString
		while (pageInfo[longitudeIndex] != ','):

				longitudeString += pageInfo[longitudeIndex]
				longitudeIndex = longitudeIndex + 1
	
		longitudeString += "],"

		coordinatesString += longitudeString

	coordinatesString += "];"





	# insterts user id in url.
	userIdIndex = url.find("&count")
	instagramUserURL = url[:userIdIndex] + "&max_id=" + maxID



	# webPage variable will hold the information from the url.
	webPage = urllib.urlopen(instagramUserURL)

	# pageinfo will hold all the data displayed on the screen with the latitude and longitude.
	pageInfo = webPage.read()


	counter = 0








# (next two comments are for debugging)
#print pageInfo
#print coordinatesString

#------------------------------------------------------creating html file-------------------------------------------------------- 



'''(COMMENT)creates an html file from a given string,
and call the default web browser to display the file.'''

contents = '''
<!DOCTYPE html>
<html> 
<head> 
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
  <title>InstaPlot</title> 
  <script src="http://maps.google.com/maps/api/js?sensor=false" 
          type="text/javascript"></script>
  <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
  </style>                
</head> 
<body>
    <div id="map"></div>
  <script type="text/javascript">
  
    var locations = 

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: new google.maps.LatLng(38.94,-98.977),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][0], locations[i][1]),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    
    }
    
  </script>
</body>
</html>
'''

#-----------------------------------------------------html string manipulation---------------------------------------------------


# adds the coordinates found previously in the instagra api url
# to the html string
index = contents.find("var locations =") + 15
newContents = contents[:index] + coordinatesString + contents[index:]

#print newContents


#-----------------------------------------------------open webPage----------------------------------------------------------------

import webbrowser, os.path

def main():
    browseLocal(newContents)


def strToFile(text, filename):
    #Write a file with the given name and the given text.
    output = open(filename,"w")
    output.write(text)
    output.close()


def browseLocal(webpageText, filename='InstaPlot.html'):
    #Start your webbrowser on a local file containing the text with given filename.
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()



# (next comment for debugging)
#print contents


