from operator import eq

class cStringUtil:
    def useFunc1(self):
        print("useFunc 1")

    def cmpWord(self, strOrigin, strComp):
        mOrigin = strOrigin.replace('\r\n', '').split(',')
        mComp = strComp.replace('\r\n', '').split(',')

        cnt = 0
        nLen = len(mOrigin)
        for idx in range(0, nLen):
            if eq(mOrigin[idx], mComp[idx]):
                # print ("{0} == {1}".format(mOrigin[idx], mComp[idx]))
                cnt += 1
            # else:
            #    print ("{0} != {1}".format(mOrigin[idx], mComp[idx]))
        return cnt

    def cmpWordEx(self, strOrigin, strComp):
        mOrigin = strOrigin.replace('\r\n', '').split(',')
        mComp = strComp.replace('\r\n', '').split(',')

        cnt = 0
        nLen = len(mOrigin)
        for idx in range(0, nLen):
            if eq(mOrigin[idx], mComp[idx]):
                # print ("{0} == {1}".format(mOrigin[idx], mComp[idx]))
                cnt += 1
            # else:
            #    print ("{0} != {1}".format(mOrigin[idx], mComp[idx]))
        return cnt, nLen

    def cmpLetter(self, strOrigin, strComp):
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
                        # print ("{0} == {1}".format(slOrigin[i], slComp[i]))
                        cnt += 1
                    # else:
                    #    print ("{0} != {1}".format(slOrigin[i], slComp[i]))

        return cnt

    def cmpLetterEx(self, strOrigin, strComp):
        mOrigin = strOrigin.replace('\r\n', '').split(',')
        mComp = strComp.replace('\r\n', '').split(',')

        cnt = 0
        nLen = len(mOrigin)
        nLength = 0

        for idx in range(0, nLen):
            slOrigin = list(mOrigin[idx])
            slComp = list(mComp[idx])
            nLength += len(slOrigin)

            for i in range(len(slOrigin)):
                if slOrigin[i] != " ":
                    if eq(slOrigin[i], slComp[i]):
                        # print ("{0} == {1}".format(slOrigin[i], slComp[i]))
                        cnt += 1
                    # else:
                    #    print ("{0} != {1}".format(slOrigin[i], slComp[i]))

        return cnt, nLength
