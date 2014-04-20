autowget
========

<h1> Overview: </h1>

Uses wget to get webpage and then saves to a file and then pushes changes to your github page

<h1> Instructions: </h1>

Fill out correct paths to wanted items. Make sure the git command "git push..." will automatically use either your SSH keys OR the correct username/password. Documentation can be found on GitHub's website or on StackOverflow or similar sites. If desired, move the autowget file to cron.daily/monthly/etc so you can let it run. Make sure permissions are correct. Additional sites can be fetched by adding the first line again, but changing the remote URL. Make sure to add more time to
the sleep counter if the sites are large.

<h1> To-Do List: </h1>

<ul>
<li>Add email confirmation</li>
<li>Append fetched URL to master directory list</li>
