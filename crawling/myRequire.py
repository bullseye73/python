 
from bs4 import BeautifulSoup
import urllib.request
import re
import pprint

#json data make
import json
from collections import OrderedDict
 
# Ready for data
group_data = OrderedDict()
top10 = OrderedDict()

OUTPUT_FILE_NAME = 'output.txt'
#URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=055&aid=0000445667'
URL = 'https://www1.president.go.kr/petitions/579682'
#TOP10_URL = 'https://news.naver.com'

# ??? ??

def get_require(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    arrData=[]
    text = {}

    title = soup.find('h3', attrs={'class':'petitionsView_title'})
    progress = soup.find('div', attrs={'class':'petitionsView_progress'})
    count = soup.find('span', attrs={'class':'counter'})

    arrData.append({ 'title': title.text ,'progress': progress.h4.text, 'count': count.text })
    
    text = arrData
    jsondata = json.dumps(text, ensure_ascii=False, indent=2)

    print(jsondata)
    print(text)
    
    return text

# 
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
    return cleaned_text

# 
def main():
    result_top = get_require(URL)
  
if __name__ == '__main__':
    main()


