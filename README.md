autowget
========

<h1> Overview: </h1>

Bash version: Uses wget to get webpage and then saves to a file and then pushes it to your GitHub page or ftps file(s) to your server.
Python version: Gets website and saves to a file and then pushes it to your GitHub page OR ftps the file(s) to your server.

<h1> Instructions: </h1>
<h3> What's needed: </h3>
<ul>
<li>wget</li>
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

<h2> To Install: </h2>

`git clone https://www.github.com/EricLagerg/autowget.git`
<p>
`cd /path/to/autowget/`
<p>
`mv autowget /place/where/you/store/scripts/`
<p>
`chmod 755 autowget`

Also, in order for the logs to work, you need to 

`cd /path/to/logs && touch name.of.logfile.log`
<p>
`chmod 666 name.of.logfile.log`

Permissions aren't set in stone. You'll just need autowget to be writable from whichever user is running the script, and you'll need autowget to be executable by whichever user you want running the script.



<h1> Documentation:</h1>

Fill out correct paths to wanted items. Make sure the git command "git push..." will automatically use either your SSH keys OR the correct username/password. Documentation can be found on GitHub's website, StackOverflow, or similar sites. If desired, move the autowget file to cron.daily/monthly/etc so you can let it run. Make sure permissions are correct.

The names are self-explanitory. autowget will grab one pagee and mirror it. autowget-directory will mirror a whole structure, so you can effectively mirror an entire website. autowget-ftp will use ftp instead of Git. autowget.py does the same thing as the other bash scripts, but uses Python3 (and is much, much faster).

Website not showing up 100% correctly? Try reading here: http://wget.addictivecode.org/FrequentlyAskedQuestions or my mirror at http://www.ericlagergren.com/projects/mirrors/wgetaddictivecodeorgFrequentlyAskedQuestions.html

Web scraping can be difficult, so read that link and tinker with the options. If it doesn't resolve, then it probably cannot be done.

<h3>If it's not working shoot me an email at contact@ericlagergren.com or create an issue. Please make sure to include logs. It's hard to troubleshoot without logs. Also include the full source code. Thanks. </h3>

<h1> To-Do List: </h1>

<ul>
<li>Append fetched URL to master directory list</li>
</ul>
