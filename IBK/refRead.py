#-*- coding: utf-8 -*-

import os, codecs
import openpyxl
import sys, re, time

def makeFileName ():
    fn = "result"
    now = time.localtime()
    s = "%04d%02d%02d_%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return fn + "_" + s + ".txt"

def readTxtFile_ex(fn):
    file_list = os.listdir(fn)
    retfilename = fn + "\\" + makeFileName()
    wf = open(retfilename, mode='wt', encoding='utf-8')

    for f in file_list:
        if f.endswith(".txt"):
            print(f)
            with codecs.open(fn+"\\"+f, 'r', encoding="utf-8-sig") as rf:
                wf.write('"set name","' + f + '"\n')
                wf.write('"file name","' + f + '"\n')
                wf.write(rf.read())
    wf.close()
    #with codecs.open(fn, 'r', encoding="utf-8-sig") as f:


def Usage():
    print ("Usage: input folder [dir name]")

def main():
    if len(sys.argv) != 2:
        Usage()
        sys.exit()

    readTxtFile_ex(sys.argv[1])

if __name__ == '__main__':
    main()