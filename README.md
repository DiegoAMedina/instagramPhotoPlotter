# InstaPlot

## Instagram Picture Location Plotter

Contributors:
	- @jeremyrudd7
	- @ThaliaVillalobos
	- @TheCosmicRay01


###Description
This python program will scan through an Instagram user's profile and pin point the location of the picture on Google maps. (If location is provided in the picture). The gui used is from the TKinter (python library), and all is ran through the terminal. A string containing java and html contains all the information to create a web page. The string is the converted to an html file and opened with webbrower (python library). Once the web browser is opened locally, you have reached the end of the program. The web page is left opened for the user to be able to browse through the map and zoom in and out as much they wish for.


### Procedure followed:

Enter an instagram user's name and scan through all their profile for geolocations of each picture posted.
Once all the locations are gathered, plot them on a map to display all the pinpoints of where their pictures were taken.
The map will open up in a local web browser using google maps to plot locations, using both instagram and google maps api.

- Get an access_token from instagram api 
	- Must have an Instagram account
- Retrieve user information with access_token to first get the user's Instagram ID number
	- Through Instagram's url endpoint search
- In the same format, once metadata is received, pull the longitude and latitude from each picture.
	- Within the same data page, find the max_id number to be able to iterate through every picture in the profile.
		- max_id will change in every page, and the last page will not contain one anymore.
	- Store all the coordinates and name of the location in a string
- Google maps api
	- add the string of coordinates to the html string inside the java script
-convert the html string to a file 
-open the new html file with webbrowser (python library)
