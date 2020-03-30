from fitparse import FitFile
import os

# the overall max speed in meter p/s
max_speed = 0.0

# loop through all fit files in directory
for filename in os.listdir(os.path.abspath(os.getcwd())):
    if filename.endswith(".fit"):
        
        # open fitfile 
        fitfile = FitFile(filename)
        
        # Get all data messages that are of type record
        for record in fitfile.get_messages('record'):

            # Go through all the data entries in this record
            for record_data in record:
                
                if record_data.name == "enhanced_speed":
                    
                    # save new max speed if higher than previous value
                    if record_data.value > max_speed:
                        max_speed = record_data.value
    
    # continue if not a fit file
    else:
        continue
        
        
print "Your max speed in KM/H is " + str(max_speed * 3.6)
print "Your max speed in M/PH is " + str(max_speed * 2.237)
