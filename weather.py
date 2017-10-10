import urllib.request
import urllib.parse
import json

def geo():
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select * from weather.forecast where woeid = 2295424 and u='c'"
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read()
    data = json.loads(result)
    weather = data['query']['results']['channel']['item']['condition']
    location = data['query']['results']['channel']['location']
    return weather,location


