from bs4 import BeautifulSoup
import urllib.request
from urllib import parse
import re
import sys
import json

from collections import OrderedDict
# json data make



# Ready for data
#group_data = OrderedDict()
#OUTPUT_FILE_NAME = 'output.txt'
URL = 'https://www.youtube.com'

#
def get_text(URL, keyword=''):
    if (len(keyword) > 0) :
        searchURL = URL + '/results?search_query=' + parse.quote(keyword)
    else :
        searchURL = URL

    source_code_from_URL = urllib.request.urlopen(searchURL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    odData = OrderedDict()
    arrData = []
    #jsonData = {}


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
        print("index[{0}], data[{1} ".format(len(arrData), jsonData))

    print("---------------------------------------------------------")

    return arrData
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

