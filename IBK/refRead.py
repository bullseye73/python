#-*- coding: utf-8 -*-

import os, codecs
import openpyxl
import sys, re, time

def makeFileName (str):
    fn = re.sub('[-=.#/?:$}]', '', str)
    now = time.localtime()
    s = "%04d%02d%02d_%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return fn + "_" + s + ".xlsx"

def readTxtFile_ex(fn):
    fi = os.path.split(fn)
    fname, ext = os.path.splitext(fi[1])

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Ref"

    with codecs.open(fn, 'r', encoding="utf-8-sig") as f:
        #titles = ["FileName","Ref.NO.", "Data"]
        xlData = list()
        isReadRef = False
        isStart = True

        #worksheet.append(titles)
        for line in f:
            r = line.replace('\r\n', '').strip()

            if "jpg" in r.lower():
                if isStart:
                    xlData.append(r)
                    isStart = False
                else:
                    worksheet.append(xlData)
                    xlData.clear()
                    xlData.append(r)
                    isReadRef = False
                    isStart = True
            elif "ref" in r.lower():
                ref = r.split(" ", 1 )
                if len(ref) <= 1:
                    isReadRef = True
                    xlData.append(r)
                else:
                    xlData.append(ref[0])
                    xlData.append(ref[1])
                    worksheet.append(xlData)
                    xlData.clear()
                    isReadRef = False
                    isStart = True
            else:
                if isReadRef:
                    xlData.append(r)
                    worksheet.append(xlData)
                    xlData.clear()
                    isReadRef = False
                    isStart = True

    workbook.save(makeFileName(fname))
    workbook.close()


def Usage():
    print ("Usage: input folder [dir name]")

def main():
    if len(sys.argv) != 2:
        Usage()
        sys.exit()

    readTxtFile_ex(sys.argv[1])

if __name__ == '__main__':
    main()