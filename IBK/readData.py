#-*- coding: utf-8 -*-

import os, codecs
import xlsxwriter
import sys

def search(dir):
    files = os.listdir(dir)
    workbook = xlsxwriter.Workbook("result.xlsx")

    for file in files:
        fullFilename = os.path.join(dir, file)
        print("is file : {0} ".format(fullFilename))
        worksheet = workbook.add_worksheet(file)

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