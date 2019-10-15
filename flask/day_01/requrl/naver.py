from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import json

class CNaver:
    # Ready for data
    def __init__(self, keyword=''):
        self.keyword = keyword
        self.URL = 'https://search.naver.com'
        
        if (len(keyword) > 0) :
            self.searchURL = self.URL + '/search.naver?query=' + parse.quote(keyword) +'&where=news&ie=utf8&sm=nws_hty' 
        else :
            self.searchURL = self.URL
    #
    def get_search_data(self):
        source_code_from_URL = urllib.request.urlopen(self.searchURL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        arrData = []

        for lt in soup.find_all('ul', attrs={'class': 'type01'}):
            #print (lt)
            for list in lt.select("li dl") :
                print (list)
                text = {}
                text['keyword'] = self.keyword
                text['title'] = list.find("a").text
                text['href'] = list.find("a").attrs['href']
                text['viewCount'] = list.find("span", attrs={'class':'_sp_each_source'}).text
                text['upDate'] = list.find("span", attrs={'class':'bar'}).text
                arrData.append(text)
            #print(arrData)
            #print('test:{0}, count:{1}'.format(text, arrData.count(text)))

        #print("---------------------------------------------------------")
        print(arrData)
        #print("---------------------------------------------------------")
        jsData = json.dumps(arrData, ensure_ascii=False)

        #return json.loads(jsData)
        return jsData