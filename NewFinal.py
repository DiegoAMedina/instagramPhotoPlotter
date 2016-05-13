# (33 Latest pictures)

# prints all the information of the user including the latitude and location.
# need to change the information into a csv file to retrieve the latitude and location.

# libraries for user information retrieval and api usage
from lxml import etree
import urllib
import webbrowser, os.path

# gui library
from Tkinter import *
from PIL import Image, ImageTk


#----------------------------------------------------------GUI-------------------------------------------------------------------
global userName

#Creating a window for the menu
root = Tk()
root.title("Instagram Mapping")
root.geometry("800x600")
root.configure(background = 'white')

class App:
    def __init__(self, master):
            bottomFrame = Frame(master)
            bottomFrame.pack(side=BOTTOM)

            self.quitButton = Button(bottomFrame, text="Quit", command=close_window, height=2, width=10)
            self.quitButton.pack(side=BOTTOM)

            self.searchButton = Button(bottomFrame, text="Search", command= self.userName, height=2, width=10)
            self.searchButton.pack(side=BOTTOM)

            imageTitle = Image.open("C:\Users\Thalia\Desktop\instagramPhotoPlotter-DiegoAMedina-patch-1\instagramPhotoPlotter-DiegoAMedina-patch-1\TitleImage.jpg")
            photo = ImageTk.PhotoImage(imageTitle)
            self.Title = Label(image=photo)
            self.Title.image = photo
            self.Title.pack()

    def userName(self):
            inputUser = Search()
            print type(userName)
            

class Search:
    def __init__(self):
        self.root = Toplevel()
        self.root.wm_title("Instagram ID")
        self.root.geometry('400x200')
        self.label = Label (self.root, text= "Please Enter Your Instagram Dispaly Name", font=("Comic Sans Ms",11))
        self.label.pack()

        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext, width=40).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Enter")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()
        
        self.quitButton = Button(self.root, text="Close", command=close_window)
        self.quitButton.pack(side=BOTTOM)

        self.root.mainloop()
      
    #Getting the user Instagram name
    def clicked1(self):
        global userName
        input1 = self.entrytext.get()
        
        userName = input1
        return userName
        

def close_window():
    root.destroy()


mainWindow = App(root)
root.mainloop()

print userName

#--------------------------------------retrieve user information (user id number)-------------------------------------------------

# will add the userName to the url to find the userName's user ID
# (concatenates userName to url)
userIdUrl= "https://api.instagram.com/v1/users/search?q=&access_token=186357295.1677ed0.6ce9f99b45fc4ecfb460fd12acc0653f"    
userNameIndex = userIdUrl.find("q=") + 2
userIdUrl = userIdUrl[:userNameIndex] + userName + userIdUrl[userNameIndex:]          
      
# webPage variable will hold the information from the url.
webPage = urllib.urlopen(userIdUrl)

# pageinfo will hold all the data displayed on the screen including the user id
# (pageInfo data type string)
pageInfo = webPage.read() 


# displays in terminal to let the user know that information is being processed
print("Retrieving user's Instagram information...")


# finds the index of where the userName's Id is located in order to retrieve the ID starting at that index
userNameIndex = pageInfo.find(userName)
userNameIndex = pageInfo.find("id", userNameIndex) + 6

userId = ""

# while loop pulls the userName's ID and adds it to the variable userId one number at a time
print ("Searching for user's instagram ID...")
while (pageInfo[userNameIndex] != '"'):
	
	userId += pageInfo[userNameIndex]
	userNameIndex = userNameIndex + 1 



#---------------------------------------retrieving user information (data from pictures)------------------------------------------


print("Searching for coordinates..")

# instagram api url to retrieve user picture information.
# and adds the userId into the url
url = "https://api.instagram.com/v1/users//media/recent/?access_token=186357295.1677ed0.6ce9f99b45fc4ecfb460fd12acc0653f&count=33"
userIdIndex = url.find("users/") + 6
instagramUserURL = url[:userIdIndex] + userId + url[userIdIndex:]

# webPage variable will hold the information from the url.
webPage = urllib.urlopen(instagramUserURL)

# pageinfo will hold all the data displayed on the screen with the latitude and longitude. (String)
pageInfo = webPage.read()

#--------------------------------------------------retrieves max_id--------------------------------------------------------------

# Instagram's api only returns the information of 33 pictures at a time.
# Every time you retrieve information, it contains a new max_id number.
# You need that max_id number to find the information of the next 33 pictures.

# finds index of the max_id number within the data from "pageInfo"
maxIdIndex = pageInfo.find("max_id=") + 7
maxID = ""

# adds the max_id number to the variable maxID
while(pageInfo[maxIdIndex] != '"'):
	maxID += pageInfo[maxIdIndex]
	maxIdIndex = maxIdIndex + 1

#--------------------------------------------------------Finds coordinates (LOOP)-------------------------------------------------


# string for entire list of coordinates.
# coordinates will be added to this string
coordinatesString = " ["

# counter variable used to find every latitude and longitude 
# used as a starting location 
counter = 0


# variable to display for user in the terminal to how many coordinates have been found
coordinatesCount = 0

# trigger to control when to exit the loop and stop searching for coordinates
# will change once you find the information of the last picture
quitLoop = 0


while (quitLoop == 0):

	# if conditions runs if you are NOT searching through the information of the last picture.
	if (pageInfo.find("max_id=") > 0):

		# loops through all the data until all the coordinates are found
		# " > 0 " so it does not become an infinite loop 
		while (pageInfo.find("latitude", counter) > 0 ):
			
			print ("Collecting coordinates:") 
			coordinatesCount = coordinatesCount + 1
			print (coordinatesCount)


			#-------------------------------------------------------finds latitude

			# finds the latitude index
			latitudeIndex = pageInfo.find("latitude", counter)
			latitudeIndex = latitudeIndex + 10

			# will make the next search continue where the last one was found
			# in order to not find the latitude you just found
			counter = latitudeIndex

			# empty string to add the latitude into type string
			latitudeString = "["

			# loop will retrieve and add the latitude location as a string to the variable latitudeString
			while (pageInfo[latitudeIndex] != ','):
		
					latitudeString += pageInfo[latitudeIndex]
					latitudeIndex = latitudeIndex + 1
		
			latitudeString += ","
	
			coordinatesString += latitudeString
		
			# -----------------------------------------------------find location name
			
			# find location name index
			locationNameIndex = pageInfo.find("name", counter)
			locationNameIndex = locationNameIndex + 8
			
			locationNameString = "'"
			
			# adds locations name to the locationNameString
			while(pageInfo[locationNameIndex] != '"'):
				locationNameString += pageInfo[locationNameIndex]
				locationNameIndex = locationNameIndex + 1	
	
			locationNameString += "',"
	
			coordinatesString += locationNameString
	
			# displays to user in terminal that location was found
			print locationNameString
			print ('\n')
	
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


		#--------------------------------------------------retrieves max_id------------------------------------------------------
		
		# finds the next max_id in order to find the information of the next picture

		maxIdIndex = pageInfo.find("max_id=") + 7
		maxID = ""

		# adds the new max_id number to the variable maxID
		while(pageInfo[maxIdIndex] != '"'):
			maxID += pageInfo[maxIdIndex]
			maxIdIndex = maxIdIndex + 1

		#--------------------------------------------------changes url with new max_id-------------------------------------------
		
		
		# inserts user id in url.
		maxIDindexURL = url.find("&count") + 9
		instagramUserURLMaxID = instagramUserURL[:maxIDindexURL] + "&max_id=" + maxID

		# webPage variable will hold the information from the url.
		webPage = urllib.urlopen(instagramUserURLMaxID)

		# pageinfo will hold all the data displayed on the screen with the latitude and longitude.
		pageInfo = webPage.read()


		# counter set back to 0 so the search for the user's information starts back at the beginning
		counter = 0


	# else runs if it is the information of the last picture
	else:

		# loops through all the data until all the coordinates are found
		# " > 0 " so it does not become an infinite loop 
		while (pageInfo.find("latitude", counter) > 0 ):
			
			print ("Collecting coordinates:") 
			coordinatesCount = coordinatesCount + 1
			print (coordinatesCount)


			#-------------------------------------------------------finds latitude

			# finds the latitude index
			latitudeIndex = pageInfo.find("latitude", counter)
			latitudeIndex = latitudeIndex + 10

			# will make the next search continue where the last one was found
			# in order to not find the latitude you just found
			counter = latitudeIndex

			# empty string to add the latitude into type string
			latitudeString = "["

			# loop will retrieve and add the latitude location as a string to the variable latitudeString
			while (pageInfo[latitudeIndex] != ','):
		
					latitudeString += pageInfo[latitudeIndex]
					latitudeIndex = latitudeIndex + 1
		
			latitudeString += ","
	
			coordinatesString += latitudeString
		
			# -----------------------------------------------------find location name
			
			# find location name index
			locationNameIndex = pageInfo.find("name", counter)
			locationNameIndex = locationNameIndex + 8
			
			locationNameString = "'"
			
			# adds locations name to the locationNameString
			while(pageInfo[locationNameIndex] != '"'):
				locationNameString += pageInfo[locationNameIndex]
				locationNameIndex = locationNameIndex + 1	
	
			locationNameString += "',"
	
			coordinatesString += locationNameString
	
			# displays to user in terminal that location was found
			print locationNameString
			print ('\n')
	
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


		#--------------------------------------------------retrieves max_id------------------------------------------------------
		
		# finds the next max_id in order to find the information of the next picture

		maxIdIndex = pageInfo.find("max_id=") + 7
		maxID = ""

		# adds the new max_id number to the variable maxID
		while(pageInfo[maxIdIndex] != '"'):
			maxID += pageInfo[maxIdIndex]
			maxIdIndex = maxIdIndex + 1

		#--------------------------------------------------changes url with new max_id-------------------------------------------
		
		
		# inserts user id in url.
		maxIDindexURL = url.find("&count") + 9
		instagramUserURLMaxID = instagramUserURL[:maxIDindexURL] + "&max_id=" + maxID

		# webPage variable will hold the information from the url.
		webPage = urllib.urlopen(instagramUserURLMaxID)

		# pageinfo will hold all the data displayed on the screen with the latitude and longitude.
		pageInfo = webPage.read()


		# counter set back to 0 so the search for the user's information starts back at the beginning
		counter = 0
		
		# set quitLoop to 1 since this is the information of the last picture
		quitLoop = 1


coordinatesString += "];"
#------------------------------------------------------creating html file-------------------------------------------------------- 



'''(COMMENT)creates an html file - string,
and calls the default web browser to display the file.'''

contents = '''
<!DOCTYPE html>
<html> 
<head> 
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
  <title></title> 
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
    
    var map = new google.maps.Map(document.getElementById('map'), 
    {
      zoom: 4,
      center: new google.maps.LatLng(38.94,-95.977),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    
    var infowindow = new google.maps.InfoWindow();
    
    var marker, i;
    
    for (i = 0; i < locations.length; i++) 
    {  
      marker = new google.maps.Marker(
      {
        position: new google.maps.LatLng(locations[i][0], locations[i][2]),
        map: map,
        animation: google.maps.Animation.DROP
      });
    
      google.maps.event.addListener(marker, 'click', (function(marker, i) 
      {
      	marker.setIcon('iconImage.png');
        	return function() 
        	{
        		infowindow.setContent(locations[i][1]);
          		infowindow.open(map, marker);
        	}
    
      })(marker, i));
    
    }
    
    function toggleBounce() 
    {
  		if (marker.getAnimation() !== null) 
  		{
    		marker.setAnimation(null);
  		} 
  		else 
  		{
    		marker.setAnimation(google.maps.Animation.BOUNCE);
  		}
	}
    
  </script>
</body>
</html>
'''

if (coordinatesCount == 0):
	print ("\n \nThere were no locations found in the instagram profile.\n\n")

#-----------------------------------------------------html string manipulation---------------------------------------------------

# adds the coordinates found previously in the instagra api url
# to the html string
index = contents.find("var locations =") + 15
newContents = contents[:index] + coordinatesString + contents[index:]

# will add the userName to the title tab in the web browser
titleIndex = contents.find("<title>") + 7
newContents = newContents[:titleIndex] + userName + newContents[titleIndex:]


#-----------------------------------------------------open webPage----------------------------------------------------------------

# main function to open the web browser
def main():
    browseLocal(newContents)


# Write a file with the given name and the given text.
# from string to a file
def strToFile(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()

# opens a local browser from the html string (local file) containing the text with given filename.
def browseLocal(webpageText, filename='InstaPlot.html'):
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac


main()
