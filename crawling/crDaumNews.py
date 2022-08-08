from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import re
import sys
#import jsonpip

from collections import OrderedDict

URL = 'https://media.daum.net/ranking/popular/'

#
def get_text(URL, keyword=''):
    if (len(keyword) > 0) :
        searchURL = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q=' + parse.quote(keyword)
    else :
        searchURL = URL
    print("searchURL=[{0}]".format(searchURL))
    source_code_from_URL = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

    if (len(keyword) > 0):
        arrData = get_search_news(soup)
    else:
        arrData = get_rank_news(soup)

    return arrData

def get_search_news(source):
    odData = OrderedDict()
    arrData = []
    print(source)
    for rf in source.select('div', attrs={'class': 'coll_cont'}):
        print(rf)
        for imglist in rf.select("ul > div > div > a img.thumb"):
            print(imglist)
            odData['thumb_img'] = imglist.attrs['src']

        for titlist in rf.select('div.cont_thumb strong a', attrs={'class': 'link_txt'}):
            odData['title'] = titlist.text
            odData['href'] = titlist.attrs['href']

        jsonData = json.dumps(odData, ensure_ascii=False)
        arrData.append(jsonData)

    return arrData

def get_rank_news(source):
    odData = OrderedDict()
    arrData = []

    for rf in source.select('ul.list_news2 li'):
        #print(rf)
        for imglist in rf.select("a img.thumb_g"):
            odData['thumb_img'] = imglist.attrs['src']

        for titlist in rf.select('div.cont_thumb strong a', attrs={'class': 'link_txt'}):
            odData['title'] = titlist.text
            odData['href'] = titlist.attrs['href']

        jsonData = json.dumps(odData, ensure_ascii=False)
        arrData.append(jsonData)

    return arrData


def Usage():
    print ("Usage: input search keyword")
#
def main():
    if len(sys.argv) != 2:
        Usage()
        print(get_text(URL))
    else:
        print(get_text(URL, sys.argv[1].encode()))

if __name__ == '__main__':
    main()

