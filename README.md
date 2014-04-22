autowget
========

<h1> Overview: </h1>

Uses wget to get webpage and then saves to a file and then pushes changes to your github page or ftps file(s) to your server

<h1> Instructions: </h1>
<h3> What's needed: </h3>
<ul>
<li>Wget</li>
</ul>

`git clone https://www.github.com/EricLagerg/autowget.git`
`cd /path/to/autowget/`
`mv autowget /place/where/you/store/scripts/`
`chmod 755 autowget`

Also, in order for the logs to work, you need to 

`cd /var/log/ && touch autowget.log`
`chmod 666 autowget.log`

Permissions aren't set in stone. You'll just need autowget to be writable from whichever user is running the script, and you'll need autowget to be executable by whichever user you want running the script.



<h1> Documentation:</h1>

Fill out correct paths to wanted items. Make sure the git command "git push..." will automatically use either your SSH keys OR the correct username/password. Documentation can be found on GitHub's website, StackOverflow, or similar sites. If desired, move the autowget file to cron.daily/monthly/etc so you can let it run. Make sure permissions are correct. Additional sites can be fetched by adding the first line again, but changing the remote URL.

<h1> To-Do List: </h1>

<ul>
<li>Add email confirmation</li>
<li>Append fetched URL to master directory list</li>
</ul>
