import csv
#csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)


with open('result.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    arrData = []
    jsData = {}
    isFirst = True
    Key = []
    for row in reader:
        if isFirst == True:
            Key = row
            isFirst=False
        else :
            jsData[Key[0]] = row[0]
            jsData[Key[1]] = row[1]
            jsData[Key[2]] = row[2]
            arrData.append(jsData)
        print(jsData)
        jsData={}
    print(arrData)    