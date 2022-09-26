#-*- coding: utf-8 -*-

import sys, os, re

BRAND_TIT = [['caribbeancom', 'carib','caribbean'], 
             ['heyzo', 'hey'],
             ['1pondo','1 pondo', '1pon', 'pondo'],
             ['fc2ppv','fc2'],
             ['SuperModelMedia', 'supermodelmedia', 'super model media','SMD','s model', 'super', 'model']
]
EXTS = ['.mp4', '.wmv', '.avi', '.mkv', '.m4v']

def makeFilename(_brand, _no, _date):
    arFileName = []
    #strFileName = ""
    arFileName.append(_brand[0])
    for i in range(len(_no)):
        arFileName.append(_no[i])
    if len(_date) != 0:
        arFileName.append(_date[0])
    
    #print("makeFileName : {}".format('_'.join(arFileName)))
    return '_'.join(arFileName)
    

def rename_file(name):
    #print("FILENAME={0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
    pt_brand = '[a-zA-Z]{2}2|[a-zA-Z]+'   # find 알파벳으로된 모든 문자열.
    pt_no = '[0-9]{6,7}-[0-9]{3,4}|[0-9]{7}-[0-9]{3}|[0-9]{7}|[a-z]{3,4}-[0-9]{2,4}' # ######-#### no 패턴
    pt_date = '20\d{2}[-|.]\d{2}[-|.]\d{2}|20\d{2}'
    strBrand = re.findall(pt_brand, name)
    strNo = re.findall(pt_no, name)
    strDate = re.findall(pt_date, name)
    print("Brand=[{}]\nNo=[{}]\nDate={}".format(strBrand, strNo, strDate))
    #print("TITLE={}".format(findTitle(strBrand)))
    return #makeFilename(findTitle(strBrand), strNo, strDate)

def findTitle(_strBrand):
    for i in range(len(_strBrand)):
        #print(">>>>{}".format(_strBrand[i]))
        for j in range(len(BRAND_TIT)):
            if _strBrand[i] in BRAND_TIT[j]:
                #print(">>>>>>{}".format(BRAND_TIT[j]))
                return BRAND_TIT[j]
    return ''

def readFileList(_dir):
    #pylist = glob(_dir + "/*.*")
    pylist = os.listdir(_dir)
    for l in pylist:
        if not (os.path.isdir(l)):
            #print("file[{0}]\n".format(l))
            filename, filext = filterFile(l)
            if filext.lower() in EXTS:
                #rename_file(filename)
                os.rename(_dir + l, _dir + rename_file(filename) + filext)
               #return

def filterFile(_path):
    fn = os.path.splitext(_path)
    #print("filename[{0}], fileext[{1}]".format(cleanText(fn[0]), fn[1]))
    return cleanText(fn[0]), fn[1]

def cleanText(readData):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣-?0-9a-zA-Z.-]+')
    text =  hangul.sub(' ', readData).lower()
    #print("file[{0}]\n".format(re.sub(' +', ' ', text.strip() )))
    text = re.sub('_+', '', text.strip())
    #text = re.sub('[_|_ ]{2,20}', '', text.strip())
    return text

def Usage():
    print("Usage: input folder [PromptID List file name]")
    # Press the green button in the gutter to run the script.

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage()
        sys.exit()
    readFileList(sys.argv[1])

                                                                                                                                                                                       
