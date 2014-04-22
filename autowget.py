###############
### IMPORTS ###
###############

import urllib.request
import shutil
from ftplib import FTP
import sh
import os
import sys
import datetime
sys.stdout = open('/var/log/autowget.log', 'w')

######################
### FILL VARIABLES ###
######################

url = 'http://www.example.org'
file_name = '/path/to/the/file'
file_path = '/path/to/the/' # Path to file's containing folder
repo = '/path/to/repo'
commitMessage = 'new mirror' # Your commit message 
addAll = '--all' # Adds all tracked files; can change to just one file
branch = 'master' # Branch you're committing/pushing to

##############################
### Uncomment if using FTP ###
##############################

#ftp = FTP('ftp.server.com')
#username = "" # FTP server username
#password = "" # FTP server password
#server_path = "" # Path to folder where you want to save file(s)

# If login is anonymous (why it would be is beyond me) then go to line 55 "ftp.login(username, password)" and delete the two words "username," and "password" so it looks like this: ftp.login()

####################################
### SHOULDN'T NEED TO TOUCH THIS ###
####################################

def getUrl():
	response = urllib.request.urlopen(url)
	with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
	   	shutil.copyfileobj(response, out_file)
getUrl()

def gitPush():
	git = sh.git.bake(_cwd=repo)
	print(git.status())
	#print(git.checkout(branch))
	print(git.add(addAll))
	print(git.commit(m=commitMessage))
	print(git.push('origin', branch))
	print(git.status())


if 'ftp' in locals():
	ftp.login(username, password)
	ftp.cwd(server_path)
	os.chdir(file_path)
	ftp.storlines("STOR " + file_name, open(file_name, 'r'))
else: 
	gitPush()

print(datetime.datetime.now().strftime("%m-%d-%y"))

