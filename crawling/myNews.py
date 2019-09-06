 
from bs4 import BeautifulSoup
import urllib.request
import re,sys


#json data make
import json
from collections import OrderedDict
 
# Ready for data
group_data = OrderedDict()
top10 = OrderedDict()

OUTPUT_FILE_NAME = 'output.txt'
#URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=055&aid=0000445667'
URL = 'https://m.news.naver.com'
TOP10_URL = 'https://news.naver.com'

# ??? ??
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text

def get_top_news(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', attrs={'class':'r_group_lft'}):
        text = text + str(item.find_all(text=True))
    return text

def get_top_10(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    i = 0
    text={}

    for category in soup.find_all('ul', attrs={'class':'section_list_ranking'}):
        ranks = soup.select('h5.blind')[i]
        i += 1
        
        arrData=[]
        #print(category)
        for title in category.select('a'):
            #print("title[{0}], href[{1}]".format(title.text, URL+title.attrs['href']))
            arrData.append({ 'title': title.text , 'url': URL+title.attrs['href'] })
        
        text[ranks.text] = arrData
        
    jsondata = json.dumps(text, ensure_ascii=False, indent=2) #, separators=(',', ': '), sort_keys=True)

    #print(jsondata)
    return jsondata

# 
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
    return cleaned_text

def Usage():
    print ("Usage: input youtube keyword")
#
def main():
    result_top = get_top_10(TOP10_URL)
    jsData = json.loads(result_top)

    if len(sys.argv) != 2:
        Usage()
        print(jsData)
    else:
        print(jsData[sys.argv[1]])



if __name__ == '__main__':
    main()


