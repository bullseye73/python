import ftplib

ftp = ftplib.FTP()
ftp.connect('', 21)
ftp.login('admin', '')
ftp.cwd('/data8T/ftpRoot')

filename = 'test.zip'
myfile = open(filename, 'rb')

ftp.storbinary('STOR' + filename, myfile)

myfile.close()
ftp.close()