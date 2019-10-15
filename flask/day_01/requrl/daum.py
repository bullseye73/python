from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import json

class CDaum:
    # Ready for data https://search.daum.net/search?w=news&q=%EC%A1%B0%EA%B5%AD&DA=ATG&spacing=0
    def __init__(self, keyword=''):
        self.keyword = keyword
        
        if (len(keyword) > 0) :
            self.URL = 'https://search.daum.net'
            self.searchURL = self.URL + '/search?w=news&q=' + parse.quote(keyword) +'&DA=ATG&spacing=0' 
        else :
            self.URL = 'https://search.daum.net'
            self.searchURL = self.URL
    #
    def get_search_data(self):
        source_code_from_URL = urllib.request.urlopen(self.searchURL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        print (soup)
        arrData = []

        for lt in soup.find_all('div', attrs={'class': 'cont_inner'}):
            print (lt)
            for list in lt.select("div", attrs={'class': 'wrap_tit mg_tit'}) :
                print (list)
                text = {}
                text['keyword'] = self.keyword
                text['title'] = list.find("a", attrs={'class':'f_link_b'}).text
                text['href'] = list.find("a", attrs={'class':'f_link_b'}).attrs['href']
                text['viewCount'] = ''#list.find("span", attrs={'class':'_sp_each_source'}).text
                text['upDate'] = ''#list.find("span", attrs={'class':'bar'}).text
                arrData.append(text)
            #print(arrData)
            #print('test:{0}, count:{1}'.format(text, arrData.count(text)))

        #print("---------------------------------------------------------")
        #print(arrData)
        #print("---------------------------------------------------------")
        jsData = json.dumps(arrData, ensure_ascii=False)

        #return json.loads(jsData)
        return jsData