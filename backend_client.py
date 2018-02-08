import ftplib
import os
import webbrowser
from tkinter import *
from tkinter import filedialog as fd

ftp = ftplib.FTP()
LARGE_FONT = ('Verdana',20)

def checkIfMain():
        print(ftp.pwd())
        return str(ftp.pwd())
        

def enterFolder_back(folderName):
	ftp.cwd(folderName)

def Connect(HOST,username,password):
	PORT = 5555
	
	return_var = ''

	try:
		ftp.connect(HOST,PORT)
		return_var = 'Connected\n'
	except ConnectionRefusedError:
		return_var = 'Sorry But The Server Might Be Down In The Moment\n'
		return(return_var)

	except OSError:
		return_var = return_var + 'Sorry...You Do Not Have an Active Internet Connection\n'
		return(return_var)

	try:
		ftp.login(username, password)
		return_var = return_var + 'You Loged In\n'
	
	except AttributeError:
		return_var = return_var + 'You Aren not connected to the Server\n'
	
	except:
		return_var = return_var + 'Sorry...Wrong Username or Password\n'
	
	return(return_var)


def createFolder(folderName):
	ftp.mkd(folderName)


def Delete(filefordelete):
	try:
		ftp.delete(filefordelete)
		listItems_back()
	except:
		warning = Tk()

		l1 = Label(warning,text='This Will Delete All The Items In The Folder',font=LARGE_FONT)
		l1.grid(column=0,row=0)


		def deleteFolder():
			warning.destroy()
			ftp.cwd(filefordelete)
			files4delete = ftp.nlst()
			for file in files4delete:
				ftp.delete(file)
			ftp.cwd('../')
			ftp.rmd(filefordelete)
			return 0

		b1 = Button(warning,text='Okay',command=deleteFolder)
		b1.grid(column=0,row=1)

		warning.mainloop()
		return 0


def download_back(FileName):

	downloadsFolder = os.path.expanduser(r'~\Downloads')

	if '.' in FileName:
		local_filename = os.path.join(downloadsFolder, FileName)
		file = open(local_filename, 'wb')
		ftp.retrbinary('RETR ' + FileName, file.write)
		return_var = 'You Downloaded {} In The Directory {}'.format(FileName,local_filename)

	else:
		downloadedFolder = r'{}\{}'.format(downloadsFolder,FileName)
		os.mkdir(downloadedFolder)
		ftp.cwd(FileName)
		file4download = ftp.nlst()
		for file in file4download:
			localFilename = os.path.join(downloadedFolder, file)
			file4writing  = open(localFilename, 'wb')
			ftp.retrbinary('RETR ' + file, file4writing.write)
		ftp.cwd('../')


def listItems_back():
	return_list = []
	files = ftp.nlst()
	for i in files:
		if i != '_DS_Store':
			return_list.append(i)
		else:
			pass
	return(return_list)


def chooseFile():
	file = fd.askopenfilename()
	tuplefd = os.path.split(os.path.abspath(file))
	direc = tuplefd[0]
	file = tuplefd[1]
	os.chdir(direc)
	try:
		f = open(file, 'rb')
		storfile = 'STOR {}'.format(file)
		ftp.storbinary(storfile, f)
		return_var = 'You Uploaded {}'.format(file)
	except AttributeError:
		return_var = 'Sorry.. You Must First Connect To The Server\n'
	return(return_var)
