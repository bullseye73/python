# _*_ coding: utf-8 _*_
import sys, codecs
from OCR.libs import cStringEx

def Usage():
    print ("Usage: file compare [file1] [file2]")

def main():
    if len(sys.argv) != 3:
        Usage()
        sys.exit()
    
    f1 = codecs.open(sys.argv[1], 'r', 'utf-8-sig')
    f2 = codecs.open(sys.argv[2], 'r', 'utf-8-sig')
    
    srcData = f1.readlines()
    cmpData = f2.readlines()

    cse = cStringEx.cStringEx()

    cntWordTotal = 0
    wordTotal = 0
    cntLetterTotal = 0
    letterTotal = 0
    cntWord = 0
    cntLetter = 0

    nlines = len(srcData)
    nCurr = 0
    
    for i in range(nlines):
        cntWord, wordTotal = cse.cmpWordEx(srcData[nCurr], cmpData[nCurr])
        #print("{0} : {1}".format(srcData[nCurr], cmpData[nCurr]))
        cntLetter, letterTotal = cse.cmpLetterEx(srcData[nCurr], cmpData[nCurr])
#        print("matching words count : {0}, {1}".format(cntWord, wordTotal))         # cntWord:정인식 갯수, wordTotal:비교 단어수
#        print("matching Letters count : {0}, {1}".format(cntLetter, letterTotal))   # cntLetter: 정인식 글자수, letterTotal:비교 글자수
        nCurr+=1
        cntWordTotal += cntWord
        cntLetterTotal += cntLetter

    cse.cprint ("[total records : %d ]=============================" %nCurr, "cyan")

    cse.cprint ("[Word Total Matched : %d ]" %cntWordTotal, "yellow")
    cse.cprint ("[Letter Total Matched : %d ]" %cntLetterTotal, "darkyellow")
    
    f1.close()
    f2.close()

if __name__ == '__main__':
    main()
