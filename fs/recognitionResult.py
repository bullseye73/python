import os
import xlsxwriter

def readFileName(path):
	workbook = xlsxwriter.Workbook('readresult_01.xlsx')
	worksheet = workbook.add_worksheet()
	filenames = os.listdir(path)

	worksheet.write('A1', 'Path')
	worksheet.write('B1', 'FileName')

	row = 1
	col = 0
	for filename in filenames:
		worksheet.write(row, col, path)
		worksheet.write(row, col+1, filename)
		row += 1
		#full_filename = os.path.join(path, filename)
		#print (full_filename)

	workbook.close()

def main():
	for i in os.listdir("./"):
		if os.path.isdir(i):
			print(i)
			readFileName(i)


if __name__ == '__main__':
    main()



