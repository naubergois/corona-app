from flask import Flask
from pymongo import MongoClient
import geocoder
import pymongo
from pymongo import MongoClient
import datetime
import pandas as pd
from folium.plugins import HeatMap
import folium
from flask import render_template


app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.corona_tracking
position = db.position

def generateBaseMap(default_location=[40.693943, -73.985880], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map

@app.route('/map/')
def map():

    
    now = datetime.datetime.now()

    cursor=position.find({"year":now.year,"month":now.month,"day":now.day})
    df =  pd.DataFrame(list(cursor))

    print(df)

    
    
    df1=df[['latitude', 'longitude']]
    print(df1)
    base_map = generateBaseMap()
    HeatMap(data=df1).add_to(base_map)
    base_map.save('plot_data.html')
    return render_template("plot_data.html")
    
   

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004)