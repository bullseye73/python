#-*- coding: utf-8 -*-

import os, codecs
import xlsxwriter
import sys, re, time

def makeFileName (str):
    fn = re.sub('[-=.#/?:$}]', '', str)
    now = time.localtime()
    s = "%04d%02d%02d_%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return fn + "_" + s + ".xlsx"

def search(dir):
    files = os.listdir(dir)
    workbook = xlsxwriter.Workbook(makeFileName(dir))

    for file in files:
        fullFilename = os.path.join(dir, file)
        print("is file : {0} ".format(fullFilename))
        fname, ext = os.path.splitext(file)
        worksheet = workbook.add_worksheet(fname)
        readTxtFile(worksheet, fullFilename)

    workbook.close()

def readTxtFile(ws, fn):
    with codecs.open(fn, 'r', encoding="utf-8-sig") as f:
        row = 0
        col = 0
        for line in f:
            r = line.replace('\r\n', '').strip()
            rData = r.replace('"', '').split(',', 1)
            rlen = len(rData)

            if rlen <= 1:
                continue

            if 'set' in rData[0].lower():
                row += 1
                col = 0
            else:
                if row == 1:
                    ws.write(row-1, col, rData[0])
                    ws.write(row , col, rData[rlen - 1])
                else:
                    ws.write(row, col, rData[rlen - 1])
                col += 1

def Usage():
    print ("Usage: input folder [dir name]")

def main():
    if len(sys.argv) != 2:
        Usage()
        sys.exit()

    search(sys.argv[1])

if __name__ == '__main__':
    main()