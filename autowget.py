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
sys.stdout = open('/var/log/autowget.log', 'a')
sys.stderr = open('/var/log/autowget.log', 'a')

######################
### FILL VARIABLES ###
######################

urls = ['http://www.example.org', 'https://google.com', 'https://microsoft.com']
file_path = '/path/to/directory/file/is/in'
repo = '/path/to/github/pages/repository' # If you only want to commit one portion of your repository, then make sure you put that path here
commitMessage = 'new mirror' # Your commit message 
addAll = '--all' # Adds all tracked files; can change to just one file
branch = 'master' # Branch you're committing/pushing to

############################################################
### FTP OPTIONS - MAKE SURE TO CHANGE THESE IF USING FTP ###
############################################################

#useFtp = True
useFtp = False
# If login is anonymous (why it would be is beyond me) then leave the password and username variables alone
username = "" # FTP server username
password = "" # FTP server password
server_path = "" # Path to folder where you want to save file(s)
server = "" # Server name... e.g. ftp.debian.org

####################################
### SHOULDN'T NEED TO TOUCH THIS ###
####################################

def getUrl(urls):
	for url in urls:
		new_file_path = file_path + url.rsplit('.com', 1)[0].replace('https://', '').replace('http://', '').replace('.', '').replace('www', '').replace('/', '') + ".html"
		response = urllib.request.urlopen(url)
		#if (os.path.isfile(new_file_path) == False): # Don't mess with this... there for potential future use
		with open(new_file_path, 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
#		'''elif (os.path.isfile(new_file_path) == True): # Same with these lines
#			for i, urls in enumerate(urls, start=0):	 # And this
#				number_name = new_file_path.replace('.html', '') + "-%s.html" % i # This too
#				with open(number_name, 'wb') as out_file:	# This one as well
#					shutil.copyfileobj(response, out_file)''' # And finally this one
getUrl(urls)

def gitPush():
	git = sh.git.bake(_cwd=repo)
	print(git.status())
	print(git.add(addAll))
	print(git.commit(m=commitMessage))
	print(git.push('origin', branch))
	print(git.status())


if useFtp == True:
	ftp = FTP(server) # FTP server... e.g. ftp.debian.org
	ftp.login(username, password)
	ftp.cwd(server_path)
	os.chdir(file_path)
	ftp.storlines("STOR " + file_path, open(file_path, 'r'))
else: 
	gitPush()

print(datetime.datetime.now().strftime("%m-%d-%y"))

