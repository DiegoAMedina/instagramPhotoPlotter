# prints all the information of the user including the latitude and location
# need to change the information into a csv file to retrieve the latitude and location

from lxml import etree
import urllib

# webPage will receive information from the url
webPage = urllib.urlopen("https://api.instagram.com/v1/users/186357295/media/recent/?access_token=186357295.1677ed0.6ce9f99b45fc4ecfb460fd12acc0653f")

#pageinfo will hold all the data displayed on the screen with the latitude and longitude
pageInfo = webPage.read()

#print pageInfo




#--------------------------------------------------------Finds latitude


# finds the latitude index
latitudeIndex = pageInfo.find("latitude")
latitudeIndex = latitudeIndex + 10

# empty string to add the latitude into type string
latitudeString = "["

# loop will retrieve and add the latitude location as a string to the variable latitudeString
while (pageInfo[latitudeIndex] != ','):

		latitudeString += pageInfo[latitudeIndex]
		latitudeIndex = latitudeIndex + 1
		
latitudeString += ","
	
#-------------------------------------------------------finds longitude

# finds the longitude index
longitudeIndex = pageInfo.find("longitude")
longitudeIndex = longitudeIndex + 11

# empty longitude to add the longitude of type string
longitudeString = ""

# loop will retrieve and add the longitude location as a string to the variable longitudeString
while (pageInfo[longitudeIndex] != ','):

		longitudeString += pageInfo[longitudeIndex]
		longitudeIndex = longitudeIndex + 1

longitudeString += "],"


#------------------------------------------------------creating html file 



'''A simple program to create an html file froma given string,
and call the default web browser to display the file.'''

contents = '''
<!DOCTYPE html>
<html> 
<head> 
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
  <title>Google Maps Multiple Markers</title> 
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

#-----------------------------------------------------html string manipulation

coordinatesString = " [" + latitudeString + longitudeString + "];"

index = contents.find("var locations =") + 15
newContents = contents[:index] + coordinatesString + contents[index:]

#print newContents


#-----------------------------------------------------open webPage

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


