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



#-----------------------------------creating html file





'''A simple program to create an html file froma given string,
and call the default web browser to display the file.'''

contents = '''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Instagram User Location</title>
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

    <script>

      function initMap() {
        var myLatLng = {lat: , lng: };


        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 10,
          center: myLatLng
        });

        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
        });
      }
      
    </script>
    <script async defer
    	src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC8SmSpDKNb3eRaklwgdNNNelvygFzDqS8&callback=initMap">
    </script>
  </body>
</html>
'''


#-------------string manipulation


index = contents.find('lat: ') + 5
newContents = contents[:index] + latitudeString + contents[index:]


index2 = contents.find('lng: ') + 9
newContents = newContents[:index2] + longitudeString + newContents[index2:]

#print newContents



def main():
    browseLocal(newContents)

def strToFile(text, filename):
    #Write a file with the given name and the given text.
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    #Start your webbrowser on a local file containing the text with given filename.
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()

#print contents





