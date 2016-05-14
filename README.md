# InstaPlot
### Instagram Picture Location Plotter


Enter an instagram user's name and scan through all their profile for geolocations of each picture posted.\n
Once all the locations are gathered, plot them on a map to display all the pinpoints of where their pictures were taken.
The map will open up in a local web browser using google maps to plot locations, using both instagram and google maps api.

- [x]Get an access_token from instagram api 
- [x]Enter user information with access_token to be able to retrieve user's picture information.
- [x]Once metadata is received, pull the longitude and latitude from each picture.
- [x]Pull the longitude and latitude from all the pictures.
	- [x]Save the longitude and latitude in an array.
- []Google maps api
	- [x]Send the longitude and latitudes gathered in the array to the map to plot the locations and display them.
	- [x]use java within an html string to then convert into a file and use it to open up the map in a web browser. 
