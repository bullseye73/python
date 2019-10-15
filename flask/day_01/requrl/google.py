from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import json

class CGoogle:
    # Ready for data https://news.google.com/search?q=%EC%A1%B0%EA%B5%AD&hl=ko&gl=KR&ceid=KR%3Ako
    def __init__(self, keyword=''):
        self.keyword = keyword
        
        if (len(keyword) > 0) :
            self.URL = 'https://news.google.com'
            self.searchURL = self.URL + '/search?q=' + parse.quote(keyword) +'&hl=ko&gl=KR&ceid=KR%3Ako' 
        else :
            self.URL = 'https://news.google.com/?tab=wn0&hl=ko&gl=KR&ceid=KR:ko'
            self.searchURL = self.URL

        print(self.searchURL)
    #
    def get_search_data(self):
        source_code_from_URL = urllib.request.urlopen(self.searchURL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        #print (soup)
        arrData = []

        for lt in soup.find_all('article', attrs={'class': 'MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne'}):
            #print (lt)
            #for list in lt.select("a", attrs={'class': 'DY5T1d'}) :
                #print (list)
            text = {}
            text['keyword'] = self.keyword
            text['title'] = lt.find('a', attrs={'class': 'DY5T1d'}).text
            text['href'] = self.URL + '/' + lt.find('a', attrs={'class': 'DY5T1d'}).get('href')
            text['viewCount'] = lt.find('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
            text['upDate'] = lt.find('time', attrs={'class': 'WW6dff uQIVzc Sksgp'}).text
            arrData.append(text)
            #print(arrData)
            #print('test:{0}, count:{1}'.format(text, arrData.count(text)))

        #print("---------------------------------------------------------")
        #print(arrData)
        #print("---------------------------------------------------------")
        jsData = json.dumps(arrData, ensure_ascii=False)

        #return json.loads(jsData)
        return jsData

