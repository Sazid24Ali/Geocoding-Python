				     SKELETON

GEOCODING
|   Error_Box.py ------------- Revertes Here When Error Occurs.
|   Geocoding_Brain.py ------- The Backend Lies Here.
|   Geocoding_Main_Win.py ---- The Frontend Lies Here.
|   readme.txt --------------- As The Name Suggests [ Currently You'r reading it ].
|   requirements.txt --------- The Modules you require to Execute This Peogram
|   
\---UI_files ------ Designed Using " Qt Designer 5.13.0 "
        Error_Box.ui             
        Geocoding_Main_Win.ui	 


          					About Project

- This Project Uses Google's Geocoding API In order To Convert The Given Address's To Coordinates.

- Google's Geocoding API : This Basically Convert The Given Address's to Cooridinates[Latitude and Longitude] and Vice-Versa(But This   
                           Project Mainly Focuses on Converting Address's to Coordinates)


                           	How To Use Project

- Run The Geocoding_Main_Win.py file ( Opens Up A Window).
- Type Or Paste The Address In the Specified Place.
- Click The 'Submit' Button Submit.
- The Frespaces Beside The Latitude and Longitude Will Be Populates With Values( They are the Coordinates ). 


      						About API KEY

- The API KEY Should be generated and placed in the Geocoding_Brain.py file at 'line:11' IN ORDER TO FUNCTION.


							Insight of Project

- When The Adress is Given By User and The  'Submit' Button is Clicked 
  -- The Data Type is copied 
  -- Copied data is Given to Geocoding_Brain.py 
  -- Here The API is Invoked and Address is sent to 'https://maps.googleapis.com/maps/api/geocode/json?paramas' using 'request' library.
  -- paramas Here are the Dictionary of API KEY and Address.
  -- The 'request' library gets the data from the API.
  -- These Data is then serialized Using 'json' library.
  -- From the json data the Latitude and the Longitude are extracted. 
  -- These extracted Coordinates Are then Converted from Decimal To DMS(Degrees,Minutes,Seconds) Format Using 'Convert' Function .
  -- These Converted data is then Populated at the Frespaces Beside The Latitude and Longitude in the Window.

- When The Adress is NOT GIVEN and The 'Submit' Button is Clicked
  -- An Error is raised and The 'Error_Box.py' is Invoked and The Error msg is displayed.

- When The Adress( WHICH DOS'T MAKE SENSE ) is Given and The 'Submit' Button is Clicked
  -- An Error is raised and The 'Error_Box.py' is Invoked and The Error msg is displayed.

  NOTE : 1) IF THE API KEY IS NOT PRESENT PROGRAM WILL NOT RUN ( SHOWS THE ADDRESS NOT FOUND ERROR WINDOW. ). 
  	 2) THE GOOGLE TRIES TO RESOLVE THE ADDRESS MAXIMUM TIMES , AT TIMES SHOWS AN ERROR.
