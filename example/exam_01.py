import os
#import xlsxwriter

sTitle = [""]

def readFileName(path):
	row = 1
	col = 0
	f = open(path, 'r')
	while True:
		line = f.readline()
		line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
		if not line: 
			break
		print("[{0}]: {1}".format(row, line))
		row += 1
	f.close()
		

def main():
	readFileName("./data.json")

if __name__ == '__main__':
    main()

