### import tkinter & os
import tkinter as Tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import sqlite3
import shutil

###GUI###

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self)
        self.master = master
        self.master.title('Move Text Files')
        self.master.geometry('{}x{}'.format(700,400))

        #buttons
        self.btnSourceDir = Button(self.master, text='Source', width=10, height=2, command=self.browseSource)
        self.btnSourceDir.grid(row=2,column=1,columnspan=2)

        self.btnNewDir = Button(self.master, text='Destination', width=10, height=2, command=self.browseDest)
        self.btnNewDir.grid(row=3, column=1,columnspan=2)

        self.btnMove = Button(self.master, text='MoveTxt', width=10, height=2, comman=self.moveTxt)#ADDCOMMAND
        self.btnMove.grid(row=4, column=1)

        #textbox
        self.txtSourcePath = Entry(self.master, text='Source Path', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.txtSourcePath.grid (row=2, column=3, columnspan=12)

        self.txtDestPath = Entry(self.master, text='Destination Path', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.txtDestPath.grid (row=3, column=3, columnspan=12)

        #list of moved txt
        self.lstList1 = Listbox(self.master,exportselection=0)
        #self.lstList1.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))
        self.lstList1.grid(row=4,column=2,rowspan=7,columnspan=7,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    #button functions
    def browseSource(self):
        self.sourcename = filedialog.askdirectory(initialdir = "/", title = "Select a Source", mustexist = (True))
        self.txtSourcePath.insert(0,self.sourcename)


    def browseDest(self):
        self.destname = filedialog.askdirectory(initialdir = "/", title = "Select a Destination", mustexist = (True))
        self.txtDestPath.insert(0,self.destname)

    def moveTxt(self):
        #create or connect to empty dB
        conn = sqlite3.connect('db_txtFiles.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_txtList( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fileName TEXT, \
                col_timeStamp DATE \
                );")
            conn.commit()
        conn.close()
        path = self.sourcename
        #listdir() to iterate through files and extract .txt files
        listDir = os.listdir(path)
        for i in listDir:
            if i.endswith('.txt'):
                time = os.path.getmtime(os.path.join(path,i))
                #print files to console with mtime
                print(i, ':', time)
                #put txt files into text box w/time
                self.lstList1.insert(0,i, ':', time)
                #put txt files into appropriate dB columns
                conn = sqlite3.connect('db_txtFiles.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("""INSERT INTO tbl_txtList \
                        (col_fileName, col_timeStamp) VALUES (?,?)""", \
                        (i,time))
                    conn.commit()
                conn.close()
                # use shutil.move(source, destination) to move files to new directory
                shutil.move(os.path.join(path,i), self.destname)
                
        

    






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
