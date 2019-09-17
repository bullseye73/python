from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import re
import sys
import json

from collections import OrderedDict

class cCrawing:
    #def __init__(self):

    def youtube_search(keyword=''):
        URL = "https://www.youtube.com"

        if (len(keyword) > 0) :
            searchURL = URL + '/results?search_query=' + parse.quote(keyword)
        else :
            searchURL = URL

        source_code_from_URL = urllib.request.urlopen(searchURL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        odData = OrderedDict()
        arrData = []


        for lt in soup.find_all('div', attrs={'class': 'yt-lockup-content'}):

            for list in lt.select("a", attrs={'class': 'yt-uix-tile-link'}) :
                odData['title'] = list.text
                odData['href'] = URL + list.attrs['href']
                break

            for l in lt.select('div ul.yt-lockup-meta-info li'):
                if ("조회수" in l.text) :
                    odData['viewCount'] = l.text
                else:
                    odData['update'] = l.text

            jsonData = json.dumps(odData, ensure_ascii=False)
            arrData.append(jsonData)
            #print("index[{0}], data[{1} ".format(len(arrData), jsonData))

        print("---------------------------------------------------------")

        return arrData

    def naver_get_top_10():
        URL = "https://news.naver.com"
        source_code_from_URL = urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        i = 0
        text = {}

        for category in soup.find_all('ul', attrs={'class': 'section_list_ranking'}):
            ranks = soup.select('h5.blind')[i]
            i += 1

            arrData = []
            # print(category)
            for title in category.select('a'):
                # print("title[{0}], href[{1}]".format(title.text, URL+title.attrs['href']))
                arrData.append({'title': title.text, 'url': URL + title.attrs['href']})

            text[ranks.text] = arrData

        jsondata = json.dumps(text, ensure_ascii=False, indent=2)  # , separators=(',', ': '), sort_keys=True)

        # print(jsondata)
        return jsondata