from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import re
import sys
# json data make
import json
from collections import OrderedDict

# Ready for data
group_data = OrderedDict()
top10 = OrderedDict()

OUTPUT_FILE_NAME = 'output.txt'

URL = 'https://www.youtube.com'
TOP10_URL = 'https://news.naver.com'


#
def get_text(URL, keyword=''):
    if (len(keyword) > 0) :
        searchURL = URL + '/results?search_query=' + parse.quote(keyword)
    else :
        searchURL = URL

    source_code_from_URL = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    #i = 0
    text = {}
    arrData = []
    #print(soup)
    '''
    for img in soup.findAll('img', attrs={'class':'style-scope yt-img-shadow'}):
        #print (img.attrs['src'])
        print(img)
        print("=============================================")
    '''
    for lt in soup.find_all('div', attrs={'class': 'yt-lockup-content'}):
        #for list in lt.select("a", attrs={'class': 'yt-uix-tile-link'}):
        #list = lt.select("a", attrs={'class': 'yt-uix-tile-link'})

        for list in lt.select("a", attrs={'class': 'yt-uix-tile-link'}) :
            #print("list:{0},{1}".format(list.text, list.attrs['href']))
            text['title'] = list.text
            text['href'] = URL + list.attrs['href']
            break

        for l in lt.select('div ul.yt-lockup-meta-info li'):
            if ("조회수" in l.text) :
                text['viewCount'] = l.text
            else:
                text['update'] = l.text
        #arrData.insert(arrData.count(text)+1, text)
        arrData.append(text)
        print(text)
        #print('test:{0}, count:{1}'.format(text, arrData.count(text)))

    print("---------------------------------------------------------")

    print(arrData)

    #jsondata = json.dumps(text, ensure_ascii=False, indent=2)  # , separators=(',', ': '), sort_keys=True)

    #print(jsondata)
    #return jsondata


#
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
    return cleaned_text

def Usage():
    print ("Usage: input youtube keyword")


#
def main():
    if len(sys.argv) != 2:
        Usage()
        print(get_text(URL))
    else:
        print(get_text(URL, sys.argv[1].encode()))



if __name__ == '__main__':
    main()


