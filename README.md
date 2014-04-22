autowget
========

<h1> Overview: </h1>

Uses wget to get webpage and then saves to a file and then pushes changes to your github page or ftps file(s) to your server

<h1> Instructions: </h1>
<h3> What's needed: </h3>
<ul>
<li>Wget</li>
<li>Python3</li>
<li>urllib.request</li>
<li>shutil</li>
<li>ftplib</li>
<li>sh</li>
<li>os</li>
<li>sys</li>
<li>datetime</li>
</ul>

<h3> Most systems have most of these libraries.</h3>

<h2> To Install </h2>

`git clone https://www.github.com/EricLagerg/autowget.git`
<p>
`cd /path/to/autowget/`
<p>
`mv autowget /place/where/you/store/scripts/`
<p>
`chmod 755 autowget`

Also, in order for the logs to work, you need to 

`cd /var/log/ && touch autowget.log`
<p>
`chmod 666 autowget.log`

Permissions aren't set in stone. You'll just need autowget to be writable from whichever user is running the script, and you'll need autowget to be executable by whichever user you want running the script.



<h1> Documentation:</h1>

Fill out correct paths to wanted items. Make sure the git command "git push..." will automatically use either your SSH keys OR the correct username/password. Documentation can be found on GitHub's website, StackOverflow, or similar sites. If desired, move the autowget file to cron.daily/monthly/etc so you can let it run. Make sure permissions are correct. Additional sites can be fetched by adding the first line again, but changing the remote URL.

<h1> To-Do List: </h1>

<ul>
<li>Add email confirmation</li>
<li>Append fetched URL to master directory list</li>
</ul>
