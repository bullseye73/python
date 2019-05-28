# _*_ coding: utf-8 _*_
import sys, codecs
from operator import eq

def Usage():
    print ("Usage: file compare [file1] [file2]")

def cmpSentence(strOrigin, strComp):
    mOrigin = strOrigin.replace('\r\n', '')
    mComp = strComp.replace('\r\n', '')

    #print ("{0} == {1}".format(mOrigin, mComp))
    return eq(mOrigin, mComp)

def cmpWord(strOrigin, strComp):
    mOrigin = strOrigin.replace('\r\n', '').split(',')
    mComp = strComp.replace('\r\n', '').split(',')
    
    cnt = 0
    nLen = len(mOrigin)
    for idx in range(0, nLen):
        if eq(mOrigin[idx], mComp[idx]):
            #print ("{0} == {1}".format(mOrigin[idx], mComp[idx]))
            cnt += 1
        #else:    
        #    print ("{0} != {1}".format(mOrigin[idx], mComp[idx]))
    return cnt

def cmpLetter(strOrigin, strComp):
    mOrigin = strOrigin.replace('\r\n', '').split(',')
    mComp = strComp.replace('\r\n', '').split(',')
    
    cnt = 0
    nLen = len(mOrigin)
    
    for idx in range(0, nLen):
        slOrigin = list(mOrigin[idx])
        slComp = list(mComp[idx])
        for i in range(len(slOrigin)):
            if slOrigin[i] != " ":
                if eq(slOrigin[i], slComp[i]):
                    #print ("{0} == {1}".format(slOrigin[i], slComp[i]))
                    cnt += 1
                #else:
                #    print ("{0} != {1}".format(slOrigin[i], slComp[i]))

    return cnt
    
def main():
    if len(sys.argv) != 3:
        Usage()
        sys.exit()
    
    f1 = codecs.open(sys.argv[1], 'r', 'utf-8-sig')
    f2 = codecs.open(sys.argv[2], 'r', 'utf-8-sig')
    
    srcData = f1.readlines()
    cmpData = f2.readlines()
    
    cntWordTotal = 0
    cntLetterTotal = 0
    #cntSentence = 0
    cntWord = 0
    cntLetter = 0
    cnt = 0
    nlines = len(srcData)
    #nCurr = 0
    
    print ("=================================")
    for i in range(nlines):
        cntWord = cmpWord(srcData[i], cmpData[i])
        #print("{0} : {1}".format(srcData[i], cmpData[i]))
        cntLetter = cmpLetter(srcData[i], cmpData[i])
        print("matching words count : {0}".format(cntWord))
        print("matching Letters count : {0}".format(cntLetter))
        #nCurr+=1
        cntWordTotal += cntWord
        cntLetterTotal += cntLetter
            
#    for comline in cmpData:
#        for srcline in srcData:
#            if cmpWord(comline, srcline):
#                cnt+=1

    print ("=================================")
    print ("Word Total Matched : %d" %cntWordTotal)
    print ("Letter Total Matched : %d" %cntLetterTotal)
    
    f1.close()
    f2.close()

if __name__ == '__main__':
    main()