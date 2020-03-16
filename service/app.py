from flask import Flask
from pymongo import MongoClient
import geocoder
import pymongo
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.corona_tracking
position = db.position



@app.route('/position/<latitude>/<longitude>/<id>')
def latitude_longitude(latitude,longitude,id):

    
    now = datetime.datetime.now()
    
    post = {"latitude": latitude,
         "longitude": longitude,
         "id": id,
         "year":now.year,
         "month":now.month,
         "day":now.day,
         "hour":now.hour,
         "minute":now.minute,
         "second":now.second}
    position.insert_one(post)
    return "OK"
   

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003)