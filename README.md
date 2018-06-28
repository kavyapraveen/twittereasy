# twittereasy
application which helps you get recent tweets of your friends
To setup flask environment do following steps:
$ mkdir myproject
$ cd myproject
$ virtualenv venv
$ mkdir flaskproject
$ pip install Flask
$flask\scripts\activate
$cd flaskproject
copy twitter_data.py to flaskproject folder
create templates folder in flaskproject
now copy home.html and get_url.html to templates folder
$python twitter_data.py
now go to browser and give 
127.0.0.1:50000/
enter your twitter username
wait for sometime
you can view result 
you may not get reult if number of friends are more
