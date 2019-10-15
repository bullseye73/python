from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import json

class CYoutube:
    # Ready for data
    def __init__(self, keyword=''):
        self.keyword = keyword
        self.URL = 'https://www.youtube.com'
        
        if (len(keyword) > 0) :
            self.searchURL = self.URL + '/results?search_query=' + parse.quote(keyword)
        else :
            self.searchURL = self.URL
        
#
    def get_youtube(self):
        
        source_code_from_URL = urllib.request.urlopen(self.searchURL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        arrData = []

        for lt in soup.find_all('div', attrs={'class': 'yt-lockup-content'}):
            text = {}
            for list in lt.select("a", attrs={'class': 'yt-uix-tile-link'}) :
                text['keyword'] = self.keyword
                text['title'] = list.text
                text['href'] = self.URL + list.attrs['href']
                break

            for l in lt.select('div ul.yt-lockup-meta-info li'):
                if ("조회수" in l.text) :
                    text['viewCount'] = l.text
                else:
                    text['upDate'] = l.text

            arrData.append(text) # (text.values())

            #print(arrData)
            #print('test:{0}, count:{1}'.format(text, arrData.count(text)))

        #print("---------------------------------------------------------")
        print(arrData)
        #print("---------------------------------------------------------")
        jsData = json.dumps(arrData, ensure_ascii=False)

        #return json.loads(jsData)
        return jsData