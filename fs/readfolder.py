import os
import xlsxwriter

def readFileName(ws,path):
	filenames = os.listdir(path)

	ws.write('A1', 'Path')
	ws.write('B1', 'FileName')

	row = 1
	col = 0
	for filename in filenames:
		ws.write(row, col, path)
		ws.write(row, col+1, filename)
		row += 1
		#full_filename = os.path.join(path, filename)
		#print (full_filename)

def main():
	workbook = xlsxwriter.Workbook('readresult_01.xlsx')
	worksheet = workbook.add_worksheet()

	for i in os.listdir("./"):
		if os.path.isdir(i):
			print(i)
			readFileName(worksheet, i)
	workbook.close()

if __name__ == '__main__':
    main()



