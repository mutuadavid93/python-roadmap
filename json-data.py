import urllib2
import json

url_data = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'

# Open the url and read the data
webUrl = urllib2.open(url_data)

if (webUrl.getCode() == 200):
    data = webUrl.read()
