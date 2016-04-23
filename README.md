# instagramPhotoPlotter

Enter an instagram user's name and scan through all their profile for geolocations of each picture posted.
Once all the locations are gathered, plot them on a map to display all the pinpoints of where their pictures were taken.

-Get an access_token and client_secret from instagram api
-Enter user information with access_token and client_secret to be able to retrieve user's metadata
-Once metadata is received, pull the longitude and latitude from it. (one picture)
-Pull the longitude and latitude from all the pictures.
	-Save the longitude and latitude in an array.
-(Google maps api or matplotlib)
	-Send the longitude and latitudes gathered in the array to the map to plot the locations and display them.
