import os
import xlsxwriter

def readFileName(wb, ws, path):
	filenames = os.listdir(path)
	bold = wb.add_format({'bold': True})
	ws.write('A1', 'Path', bold)
	ws.write('B1', 'FileName', bold)
	row = 1
	col = 0

	for filename in filenames:
		fname, ext = os.path.splitext(filename)
		if ext.lower() in ['.jpg', '.jpeg','.png','.gif']:
			ws.write(row, col, path)
			ws.write(row, col+1, filename)
			row += 1
		#full_filename = os.path.join(path, filename)
		#print (full_filename)
	ws.write(row, 0, 'Total', bold)
	ws.write(row, 1, '=counta(B2:B'+str(row)+')', bold)

def main():
	for i in os.listdir(os.getcwd()):
		if os.path.isdir(i):
			rf = i + '.xlsx'
			print(rf)
			workbook = xlsxwriter.Workbook(rf)
			worksheet = workbook.add_worksheet()
			readFileName(workbook, worksheet, i)
			workbook.close()

if __name__ == '__main__':
    main()

