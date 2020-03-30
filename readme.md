# Calculate Strava Max Speed
This script is intended to calculate your overall max speed in Strava. It currently does so over all activities ever. I am working on a version that can filter based on activity type. The script will output your max speed in both km/h and mp/h. 

# Howto

1. Download your Strava data. Follow the instructions on [this](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export "Bulk Download Strava Data") page to bulk download all your Strava activities. 
1. Unzip all .fit files and move them over to a separate directory. (Tip on a mac you can just simply select them all and double click). 
1. Download the python script and move it into the same directory as your .fit files
1. Run the python script (this make take a while depending on the number of activities (.fit files). For the script to work you will need to have the python fitparse library, available [here](http://dtcooper.github.io/python-fitparse/ "Fit Parse Library").

