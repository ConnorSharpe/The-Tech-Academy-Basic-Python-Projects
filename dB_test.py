import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
fileLst = list(fileList)
txtList = []

conn = sqlite3.connect('txt.db')

def newList():
    for file in fileLst:
        if file.endswith('.txt'):
            txtList.append(file)
    print(txtList)

def txtExtract():
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT \
            )")
        conn.commit()
        for i in range(len(txtList)):
            cur.execute("INSERT INTO tbl_txt (col_fileName) \
                VALUES (?)", (txtList[i],))
        conn.commit()
    conn.close()



#for i in range(len(list1)):
 #   c.execute("INSERT INTO Master (Column1, Column2, Column3, Column4,Column5)"
  #            " VALUES (?, ?, ?, ?, ?)",
   #           (list1[i], list2[i], list3[i], list4[i], list5[i]))








if __name__ == "__main__":
    newList()
    txtExtract()
