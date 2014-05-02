###############
### IMPORTS ###
###############

import urllib.request
import subprocess
import shutil
from ftplib import FTP
import sh
import os
import sys
import datetime


######################
### FILL VARIABLES ###
######################

urls = ['http://www.example.org', 'https://google.com', 'https://wwww.microsoft.com']
file_path = '/path/to/directory/where/files/will/go'
repo = '/path/to/github/pages/repository'
commitMessage = 'new mirror' # Your commit message 
addAll = '--all' # Adds all tracked files; can change to just one file
branch = 'master' # Branch you're committing/pushing to
email = "mutt -s 'Subject' user@host.com < /dev/null" # Sends email if mirror successful
logFile = "/var/log/autowget.log"


############################################################
### FTP OPTIONS - MAKE SURE TO CHANGE THESE IF USING FTP ###
############################################################

#useFtp = True
useFtp = False
# If login is anonymous (why it would be is beyond me) then leave the password and username variables alone
username = "" # FTP server username
password = "" # FTP server password
server_path = "" # Path to folder where you want to save file(s)

#######################################################
### SHOULDN'T NEED TO TOUCH THIS EXCEPT FTP PORTION ###
#######################################################

sys.stdout = open(logFile, 'a')
sys.stderr = open(logFile, 'a')

def getUrl(urls):
	for url in urls:
		new_file_path = file_path + url.rsplit('.com', 1)[0].replace('https://', '').replace('http://', '').replace('.', '').replace('www', '').replace('/', '') + ".html"
		response = urllib.request.urlopen(url)
		#if (os.path.isfile(new_file_path) == False):
		with open(new_file_path, 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		'''elif (os.path.isfile(new_file_path) == True):
			for i, urls in enumerate(urls, start=0):
				number_name = new_file_path.replace('.html', '') + "-%s.html" % i
				with open(number_name, 'wb') as out_file:
					shutil.copyfileobj(response, out_file)'''
getUrl(urls)

def gitPush():
	git = sh.git.bake(_cwd=repo)
	print(git.add(addAll))
	print(git.commit(m=commitMessage))
	print(git.push('origin', branch))
	print(git.status())
	try:
		process = subprocess.Popen(email, stdout=subprocess.PIPE, shell=True)
	except OSError:
		print("%s not working" % mutt)
pass

if useFtp == True:
	ftp = FTP('ftp.debian.org') # FTP server... e.g. ftp.debian.org
	ftp.login(username, password)
	ftp.cwd(server_path)
	os.chdir(file_path)
	ftp.storlines("STOR " + file_path, open(file_path, 'r'))
else: 
	gitPush()

print(datetime.datetime.now().strftime("%m-%d-%y"))

