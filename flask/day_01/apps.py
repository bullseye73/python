from flask import Flask, render_template

import re
import sys
# json data make

from requrl.youtube import CYoutube
from requrl.naver import CNaver
from requrl.daum import CDaum
from requrl.google import CGoogle

app = Flask(__name__)


@app.route('/<username>')
def show_user(username):
    return username

#@app.route("/") #decorator
@app.route("/youtube/<category>") 
def youtube(category):
    site = CYoutube(category)
    result = site.get_youtube()
    
    #return render_template('view.html', result=result)
    return result

@app.route("/naver/news/<category>") 
def naver(category):
    site = CNaver(category)
    result = site.get_search_data()
    
    #return render_template('view.html', result=result)
    return result

@app.route("/daum/news/<category>") 
def daum(category):
    site = CDaum(category)
    result = site.get_search_data()
    
    #return render_template('view.html', result=result)
    return result

@app.route("/google/news/<category>") 
def google(category):
    site = CGoogle(category)
    #site = CGoogle()
    result = site.get_search_data()
    
    #return render_template('view.html', result=result)
    return result

if __name__=="__main__":
    app.run(host='0.0.0.0', port='5000')    