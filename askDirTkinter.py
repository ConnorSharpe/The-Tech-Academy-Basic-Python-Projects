#For this drill, you will need to write a script that creates a GUI
#with a button widget and a text widget. Your script will also include
#a function that when it is called will invoke a dialog modal which will
# allow users with the ability to select a folder directory from their system.
#Finally, your script will show the user’s selected directory path into
#the text field.

#Your script will need to use Python 3 and the Tkinter module.

#Your script will need to use the askdirectory() method from the Tkinter module.

#Your script will need to have a function linked to the button widget
#so that once the button has been clicked will take the user’s selected
#file path retained by the askdirectory() method and print it within
#your GUI’s text widget.

import tkinter as Tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self)
        self.master = master
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Ask Directory Method')

        #button
        self.btnFilePath = Button(self.master, text='Find File Path', width=10, height=2, command=self.browseDir)
        self.btnFilePath.grid(row=2,column=1)

        #textbox
        self.txtFilePath = Entry(self.master, text='File Path', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.txtFilePath.grid (row=2, column=2, columnspan=12)

    def browseDir(self):
        self.filename = filedialog.askdirectory(initialdir = "/", title = "Select a File", mustexist = (True))
        self.txtFilePath.insert(0,self.filename)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
