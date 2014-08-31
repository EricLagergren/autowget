###############
### IMPORTS ###
###############

from datetime import datetime
from ftplib import FTP
from os import chdir, remove
import sh
from shutil	import copyfileobj
from subprocess import call
from sys import stdout, stderr
import urllib.request


######################
### FILL VARIABLES ###
######################

# A list of URLs you want to fetch
urls = ['http://www.example.org', 'https://google.com', 'https://wwww.microsoft.com']

# Base path to wherever you'd like the files to go
file_path = '/path/to/directory'

# Path to GitHub 
repo = '/path/to/github/pages/repository'

# Your commit message
commit_message = 'new mirror' 

# Adds all tracked files; can change to just one file
add_all = '--all'

# Branch you're committing/pushing to
branch = 'master'

# Sends email if mirror successful
# Can use service other than mutt
email_service = ''
subject = ''
email_address = 'user@host.org'
email = "{0} -s '{1}' {2} < /dev/null".format(email_service, subject, email_address)

# File to write log to
log_file = "/var/log/autowget.log"


############################################################
### FTP OPTIONS - MAKE SURE TO CHANGE THESE IF USING FTP ###
############################################################

# Uncomment to use FTP
#useFtp = True
# If login is anonymous (why it would be is beyond me) then leave the password and username variables alone
server = '' # FTP server... e.g. ftp.debian.org
username = '' # FTP server username
password = '' # FTP server password
server_path = '' # Path to folder where you want to save file(s)

#######################################################
### SHOULDN'T NEED TO TOUCH THIS EXCEPT FTP PORTION ###
#######################################################

stdout = open(log_file, 'a')
stderr = open(log_file, 'a')

def getUrl(urls):

	for url in urls:
		new_file_path = '{0}{1}{2}'.format(file_path, url, '.html')
		response = urllib.request.urlopen(url)

		with open(new_file_path, 'wb') as out_file:
			try:
				copyfileobj(response, out_file)
			except OSError:
				remove(new_file_path)
				copyfileobj(response, out_file)

getUrl(urls)

def git_push():
	git = sh.git.bake(_cwd=repo)
	print git.add(add_all)
	print git.commit(m=commit_message)
	print git.push('origin', branch)
	print git.status()
	try:
		call[(email)]
	except OSError:
		print '{0} not working'.format(email_service)
pass

if useFtp:
	ftp = FTP(server)
	ftp.login(username, password)
	ftp.cwd(server_path)
	chdir(file_path)
	ftp.storlines('STOR {0}'.format(file_path), open(file_path, 'rb'))
else: 
	git_push()

print datetime.now().strftime("%m-%d-%y")

