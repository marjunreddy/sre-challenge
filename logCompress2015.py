## logRetentionCompress.py
##
## Description:
##  This script is intended to compress log files on the log
##  retention server that are older than X days old.  In the 
##  script itself you specify two values, and it does the rest.
##
##     retentionLocation = folder where logs are to be archived
##     daysOnServer = Amount of days of logs to leave uncompressed
##
## Original Creation Date: 07/21/2015
## By Mallikarjuna Madireddy
## Revision History:
## - 2015/07/21 - mallikarjuna.madireddy  - Creation
## -------------------
## TODO:
##
################################################################

import os,time,string,re,subprocess
import datetime as dt


#Set some Base Variables
retentionLocation = "e:\LogRetention"
#retentionLocation = "e:\logtest"
daysUncompressed = 30;
path = os.path.normpath(retentionLocation)

#Change Directory to retention location
os.chdir(retentionLocation)

#Retain archive directories over daysUncompressed days old
offsetDate=dt.date.today() - dt.timedelta(days=daysUncompressed)
offsetDateStr = dt.date.strftime(offsetDate,"%Y%m%d");

for dir in os.listdir(path):
	fullPath =  path + "\\" + dir
	pattern = re.compile("^2015[0-9]+$")
	#Make sure pattern is all numeric
	if pattern.match(dir):
		#Verify it's older than the date in daysUncompressed
		if int(dir) < int(offsetDateStr):
			epochTime=str(int(time.time()))
			zipFileName = ""+dir+"_"+epochTime+".tar.gz"
			compressCommand="tar zcvf "+zipFileName+" "+dir+" --remove-files"
			print("Archiving (",fullPath,")")
			print("  Compress line: ",compressCommand,"")
			os.system(compressCommand)
		else:
			print("Keeping (",fullPath,")")
