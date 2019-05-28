import codecs

fileObj = codecs.open("result.csv", "r", "utf-8-sig")
u = fileObj.readlines()
lcnt = len(u)
jsData = {}
rowData = []
KeyRow = True
Key = []

for i in u :
    if KeyRow == True:
        Key = i.replace('\r\n', '').split(',')
        KeyRow=False
    else :
        rowData = i.replace('\r\n', '').split(',')
        jsData[Key[0]] = rowData[0]
        jsData[Key[1]] = rowData[1]
        jsData[Key[2]] = rowData[2]
        print(jsData)
