from flask import Flask, render_template
from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import re
import sys
# json data make
import json
from collections import OrderedDict

app = Flask(__name__)
# Ready for data
group_data = OrderedDict()
top10 = OrderedDict()

#
def get_youtube(URL, keyword=''):
    if (len(keyword) > 0) :
        searchURL = URL + '/results?search_query=' + parse.quote(keyword)
    else :
        searchURL = URL

    source_code_from_URL = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

    arrData = []

    for lt in soup.find_all('div', attrs={'class': 'yt-lockup-content'}):
        text = {}
        for list in lt.select("a", attrs={'class': 'yt-uix-tile-link'}) :
            text['title'] = list.text
            text['href'] = URL + list.attrs['href']
            break

        for l in lt.select('div ul.yt-lockup-meta-info li'):
            if ("조회수" in l.text) :
                text['viewCount'] = l.text
            else:
                text['update'] = l.text

        arrData.append(text) # (text.values())

        #print(arrData)
        #print('test:{0}, count:{1}'.format(text, arrData.count(text)))

    #print("---------------------------------------------------------")
    #print(arrData)
    #print("---------------------------------------------------------")
    jsData = json.dumps(arrData)

    return json.loads(jsData)

@app.route('/<username>')
def show_user(username):
    return username

#@app.route("/") #decorator
@app.route("/youtube/<category>") 
def apps(category):
    result = get_youtube('https://www.youtube.com', category)
    #return str(result)
    return render_template('view.html', result=result)



if __name__=="__main__":
    app.run(host='0.0.0.0', port='5000')    