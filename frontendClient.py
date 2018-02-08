from tkinter import *
from tkinter import filedialog as fd
import socket
import backend_client

empty = '                  '
LARGE_FONT = ('Verdana',20)
MEDIUM_FONT = ('Verdana',15)
SMALL_FONT = ('Calibri (Body)',10)

#Command Functions

def goBack():
        backend_client.enterFolder_back('../')
        t1.insert(END,'You Went To The Previous Folder\n')
        listItems()

def doubleClick():
        backend_client.enterFolder_back(selected_tuple)
        t1.insert(END,'You Entered Folder {}\n'.format(selected_tuple))
        listItems()

def upload():
        backend_client.chooseFile()
        listItems()

def delete():
        global selected_tuple
        backend_client.Delete(selected_tuple)
        t1.insert(END,'Deleted: {}\n'.format(selected_tuple))
        listItems()

def Connect():
        global Le1, Le2, loginWindow
        global connectionValue
        connectionValue = False

        rVal = backend_client.Connect('insert your ip address',Le1.get(),Le2.get())

        if 'Sorry' in rVal:
                error(rVal)
        else:
                connectionValue = True
                loginWindow.destroy()

def Download():
        global selected_tuple
        instertedString = backend_client.download_back(selected_tuple)
        t1.insert(END,'Downloaded Item\nSaved In The Downloads Folder\n')

def listItems():
        list_items = backend_client.listItems_back()
        list1.delete(0,END)
        t1.insert(END, 'You Listed the Server Items\n')
        for item in list_items:
                if '.' in item:
                        list1.insert(END, item)
                else:
                        item += '                     (Folder)'
                        list1.insert(END, item)

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    if '              (Folder)' in selected_tuple:
            selected_tuple = selected_tuple[:-29]       

def Clear():
        t1.delete(1.0,END)

#--------------------------------------------------------------------------

def error(text2print):
        errorWindow = Tk()

        l1 = Label(errorWindow,text=text2print,font=MEDIUM_FONT)
        l1.grid(column=0,row=0)

        errorWindow.mainloop()


def mainActivity():
        global mainActivity
        mainActivity = Tk()

        photo = PhotoImage(file='logo.png')
        photoLabel = Label(mainActivity,image=photo)
        photoLabel.grid(column=1,row=1)

        empty1 = Label(mainActivity,text=empty)
        empty1.grid(column=0,row=0)

        empty2 = Label(mainActivity,text=empty)
        empty2.grid(column=2,row=0)

        empty3 = Label(mainActivity,text='')
        empty3.grid(column=1,row=4)

        l1 = Label(mainActivity,text='RaspBattery Project',font=MEDIUM_FONT)
        l1.grid(column=1,row=2)

        b1 = Button(mainActivity,text='Login',command=loginWindow)
        b1.grid(column=1,row=3)

        mainActivity.mainloop()


def loginWindow():
        global mainActivity
        mainActivity.destroy()

        global loginWindow
        loginWindow = Tk()

        Ll1 = Label(loginWindow,text='Username')
        Ll1.grid(column=0,row=0)

        global Le1
        Le1 = Entry(loginWindow)
        Le1.grid(column=1,row=0)

        Ll2 = Label(loginWindow,text='PassWord')
        Ll2.grid(column=0,row=1)

        global Le2
        Le2 = Entry(loginWindow)
        Le2.grid(column=1,row=1)

        Lb1 = Button(loginWindow,text='Login',command=Connect)
        Lb1.grid(column=1,row=2)

        loginWindow.mainloop()


def folderWindow():
        global folderWindow
        folderWindow = Tk()

        l1 = Label(folderWindow,text='Folder Name',font=MEDIUM_FONT)
        l1.grid(column=1,row=0)

        e1 = Entry(folderWindow)
        e1.grid(column=1,row=1)

        def callback():
                backend_client.createFolder(e1.get())
                t1.insert(END,'Created Folder: {}\n'.format(e1.get()))
                folderWindow.destroy()
                listItems()

        b2 = Button(folderWindow,text='Create Folder',command=callback)
        b2.grid(column=1,row=2)

        folderWindow.mainloop()

#Main Function
        
mainActivity()

global connectionValue
if connectionValue == True:
        homeActivity = Tk()

        photo = PhotoImage(file='logo.png')
        photoLabel = Label(homeActivity,image=photo)
        photoLabel.grid(column=0,row=0)

        list1 = Listbox(homeActivity,height=15,width=35)
        list1.grid(row=1,column=0,rowspan=7)
        list1.bind('<<ListboxSelect>>', get_selected_row)
        list1.bind('<Double-1>', doubleClick)

        l1 = Label(homeActivity,text='Console')
        l1.grid(column=2,row=1)

        t1 = Text(homeActivity,height=15,width=35)
        t1.grid(column=2,row=1,rowspan=7)
        t1.config(highlightbackground="grey")
        t1.insert(END, 'Connected\n')

        b1 = Button(homeActivity,text='List Items',command=listItems,font=SMALL_FONT)
        b1.grid(column=1,row=1)

        b2 = Button(homeActivity,text='Create Folder',command=folderWindow)
        b2.grid(column=1,row=2)

        b3 = Button(homeActivity,text='Delete File',command=delete)
        b3.grid(column=1,row=3)

        b4 = Button(homeActivity,text='Download',command=Download)
        b4.grid(column=1,row=4)

        b5 = Button(homeActivity,text='Upload File',command=upload)
        b5.grid(column=1,row=5)

        b6 = Button(homeActivity,text='Enter Folder',command=enterFolder)
        b6.grid(column=1,row=6)

        b7 = Button(homeActivity,text='Previous Folder',command=goBack)
        b7.grid(column=1,row=7)

        homeActivity.mainloop()
