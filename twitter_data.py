from flask import Flask,render_template,request
import tweepy
import time 
import sqlite3
import json
import re
import urllib.response as urllib2
app=Flask(__name__)
@app.route('/')
def home():
  return render_template('home.html')
@app.route('/get_url',methods=['POST','GET'] )
def  get_url():
  if request.method=='POST':
    username=request.form["name"]
  db = sqlite3.connect("MyDB.db")
  cursor = db.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS Urls(name text, url text)")
  db.commit()
# Fill the X's with the credentials obtained by 
# following the above mentioned procedure.
  consumer_key = 'NeRxJJYlDynpxUmS1NNJgHdsi'
  consumer_secret ='74LBJPkg6WG7sHRpc5VZzdI5My2N3phNFaStB5WaHqY1Lv5B8h' 
  access_key = '898360776909406208-OqyjISyyBdGXhWh5K0RxFKvqQDf4KkW' 
  access_secret = 'Vc4QNzS2EGQdui5zIMOLlHlHePSxoWtHSBIXdui4O8onp' 
 
         
        # Authorization to consumer key and consumer secret
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
  auth.set_access_token(access_key, access_secret)
 
        # Calling api
  api = tweepy.API(auth)
  friends=tweepy.Cursor(api.friends_ids,screen_name=username,wait_on_rate_limit=True).items()
  for friend in friends:    
    for status in tweepy.Cursor(api.user_timeline,id=friend,count=1).items(1):
          urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',status.text )
          for url in urls:
            try:
              #res = urllib2.urlopen(url)
              #actual_url = res.geturl()
              cursor.execute("INSERT INTO Urls(name,url) VALUES(?,?)",(status.user.screen_name.encode('utf-8'), url))
            except:
              cursor.execute("INSERT INTO Urls(name,url) VALUES(?,?)",(status.user.screen_name.encode('utf-8'), "none"))
  
  cursur = db.cursor()
  rows=[]
  for object in cursur.execute("select * from Urls"): 
    rows.append(object)
  cursur.execute("drop table Urls")
  db.close()
  return render_template("get_url.html",objects=rows)
if __name__=='__main__':
  app.run(debug=True)         
    