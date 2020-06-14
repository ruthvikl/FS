import os
import re
from tkinter import Toplevel,Label,Listbox,END,Tk,Entry,Button,simpledialog

class Text_search :
    def txt_search():
        ROOT = Tk()
        ROOT.withdraw()
        USER_INP = simpledialog.askstring(title="Enter the string",
                                  prompt="Enter the string to search:")
        newWindow1 = Toplevel(window)
        file_number = 0
        string1= USER_INP
        lb = Listbox(newWindow1,height=100, width=100)
        path1= "C:/Users/ruthv/Desktop/FS/Records/"
        file_number = 0
        files = [f for f in os.listdir(path1) if os.path.isfile(path1+"/"+f)]
        for file in files:
            file_t = open(path1+"/"+file)
            file_text= file_t.read()
            if re.search(string1, file_text):
                m ="The text "+string1+" found in "+file
                lb.insert(END,m)
        file_number=file_number+1
        lb.grid(column=0, row=1)
        newWindow1.mainloop()  
        
    def txt_search1():
        ROOT = Tk()
        ROOT.withdraw()
        USER_INP = simpledialog.askstring(title="Enter the string",
                                  prompt="Enter the string to search:")
        newWindow1 = Toplevel(window)
        file_number = 0
        string1= USER_INP
        lb = Listbox(newWindow1,height=100, width=100)
        path1= "C:/Users/ruthv/Desktop/FS/Records/"
        files = [f for f in os.listdir(path1) if os.path.isfile(path1+"/"+f)]
        for file in files:
            file_t = open(path1+"/"+file)
            file_text= file_t.read()
            file_text=file_text.lower()
            file_t.close()
            if re.search(string1, file_text):
                m ="The text "+string1+" found in "+file
                lb.insert(END,m)
        file_number=file_number+1
        lb.grid(column=0, row=1)
        newWindow1.mainloop()  
        
    def txt_search_m():
        ROOT = Tk()
        ROOT.withdraw()
        USER_INP = simpledialog.askstring(title="Enter the string",
                                  prompt="Enter the string to search:")
        newWindow1 = Toplevel(window)
        file_number = 0
        string1= USER_INP
        lb = Listbox(newWindow1,height=100, width=100)
        path1= "C:/Users/ruthv/Desktop/FS/Records/"
        files = [f for f in os.listdir(path1) if os.path.isfile(path1+"/"+f)]
        file_number = 0
        for file in files:
            file_t = open(path1+"/"+file)
            line_number=1
            flag_file = 0
            for line1 in file_t:
                if re.search(string1, line1):
                    flag_file= 1
                    m ="The text "+string1+" found in "+file+" at line number"+str(line_number)
                    lb.insert(END,m)
                line_number=line_number+1
            if flag_file == 1:
                file_number=file_number+1
                flag_file=0
            file_t.close()
        lb.grid(column=0, row=1)
        newWindow1.mainloop()  
        
    def txt_search_m1():
        ROOT = Tk()
        ROOT.withdraw()
        USER_INP = simpledialog.askstring(title="Enter the string",
                                  prompt="Enter the string to search:")
        newWindow1 = Toplevel(window)
        file_number = 0
        string1= USER_INP
        lb = Listbox(newWindow1,height=100, width=100)
        path1= "C:/Users/ruthv/Desktop/FS/Records/"
        files = [f for f in os.listdir(path1) if os.path.isfile(path1+"/"+f)]
        file_number = 0
        for file in files:
            file_t = open(path1+"/"+file)
            line_number=1
            flag_file = 0
            for line1 in file_t:
                line1 = line1.lower()
                if re.search(string1, line1):
                    flag_file= 1
                    m ="The text "+string1+" found in "+file+" at line number"+str(line_number)
                    lb.insert(END,m)
                line_number=line_number+1
            if flag_file == 1:
                file_number=file_number+1
                flag_file=0
            file_t.close()        
        lb.grid(column=0, row=1)
        newWindow1.mainloop()  
        
    def txt_search_r():
        ROOT = Tk()
        ROOT.withdraw()
        USER_INP = simpledialog.askstring(title="Enter the string",
                                  prompt="Enter the string to search:")
        newWindow1 = Toplevel(window)
        file_number = 0
        string1= USER_INP
        lb = Listbox(newWindow1,height=100, width=100)
        path1= "C:/Users/ruthv/Desktop/FS/Records/"
        file_number = 0
        for root, dir, files in os.walk(path1, topdown = True):
            files = [f for f in files if os.path.isfile(root+"/"+f)]
            file_number = 0
            for file in files:
                file= root+file
                file_t = open(file)
                line_number=1
                flag_file = 0
                for line1 in file_t:
                    if re.search(string1, line1):
                        flag_file= 1
                        m ="The text "+string1+" found in "+file+" at line number"+str(line_number)
                        lb.insert(END,m)
                    line_number=line_number+1
            if flag_file == 1:
                file_number=file_number+1
                flag_file=0
            file_t.close()
        lb.grid(column=0, row=1)
        newWindow1.mainloop()  
        
    def txt_search_r1():
        ROOT = Tk()
        ROOT.withdraw()
        USER_INP = simpledialog.askstring(title="Enter the string",
                                  prompt="Enter the string to search:")
        newWindow1 = Toplevel(window)
        file_number = 0
        string1= USER_INP
        lb = Listbox(newWindow1,height=100, width=100)
        path1= "C:/Users/ruthv/Desktop/FS/Records/"
        for root, dir, files in os.walk(path1, topdown = True):
            files = [f for f in files if os.path.isfile(root+"/"+f)]
            file_number = 0
            for file in files:
                file_s = file
                file= root+file
                file_t = open(file)
                line_number=1
                flag_file = 0
                for line1 in file_t:
                    line1=line1.lower()
                    if re.search(string1, line1):
                        flag_file= 1
                        m ="The text "+string1+" found in "+file_s+" at line number"+str(line_number)
                        lb.insert(END,m)
                        line_number=line_number+1
                if flag_file == 1:
                    file_number=file_number+1
                    flag_file=0
            file_t.close()
        lb.grid(column=0, row=1)
        newWindow1.mainloop()        
        
    def replaceall():
        path = "C:/Users/ruthv/Desktop/FS/Records/"
        dir_list = os.listdir(path)
        newWindow2 = Toplevel(window)
        a = "Files and directories in "+ path+ ":"
        l2 = Label(newWindow2, text = a)
        l2.grid(column=0, row=1)
        lb1 = Listbox(newWindow2)
        for item in dir_list:
            lb1.insert(END,item)
        lb1.grid(column=0)
        label1 = Label(newWindow2, text='Enter the file name from the list')
        label1.grid(column=0, row=10)
        entry1 = Entry (newWindow2) 
        entry1.grid(column=0, row=11)
        label2 = Label(newWindow2, text='Enter the string to search')
        label2.grid(column=0, row=12)
        entry2 =Entry (newWindow2) 
        entry2.grid(column=0, row=13)
        label2 = Label(newWindow2, text='Enter the replace string')
        label2.grid(column=0, row=14)
        entry3 =Entry (newWindow2) 
        entry3.grid(column=0, row=15)
        def reply ():
            file = entry1.get()
            string1 = entry2.get()
            rtxt = entry3.get()
            if file in dir_list:
                file = path+file
                file_t=open(file,"r")
                data = file_t.read()
                data = data.replace(string1, rtxt)
                file_t.close
                file_t=open(file,"w")
                file_t.write(data)
                file_t.close()
                label3 = Label(newWindow2, text='Success')
                label3.grid(column=0, row=17)
            else:
                label3 = Label(newWindow2, text='Enter proper file name')
                label3.grid(column=0, row=17)
        button1 = Button(newWindow2,text='Replace all the words', command=reply, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        button1.grid(column=0, row=16)

    def replaceocc():
        path = "C:/Users/ruthv/Desktop/FS/Records/"
        dir_list = os.listdir(path)
        newWindow2 = Toplevel(window)
        a = "Files and directories in "+ path+ ":"
        l2 = Label(newWindow2, text = a)
        l2.grid(column=0, row=1)
        lb1 = Listbox(newWindow2)
        for item in dir_list:
            lb1.insert(END,item)
        lb1.grid(column=0)
        label1 = Label(newWindow2, text='Enter the file name from the list')
        label1.grid(column=0, row=10)
        entry1 = Entry (newWindow2) 
        entry1.grid(column=0, row=11)
        label2 = Label(newWindow2, text='Enter the string to search')
        label2.grid(column=0, row=12)
        entry2 =Entry (newWindow2) 
        entry2.grid(column=0, row=13)
        label2 = Label(newWindow2, text='Enter the replace string')
        label2.grid(column=0, row=14)
        entry3 =Entry (newWindow2) 
        entry3.grid(column=0, row=15)
        label2 = Label(newWindow2, text='Enter the line number')
        label2.grid(column=0, row=16)
        entry4 =Entry (newWindow2) 
        entry4.grid(column=0, row=17)
        def reply ():
            file = entry1.get()
            string1 = entry2.get()
            if file in dir_list:
                file1 = path+"1"+file
                file = path+file
                file_t=open(file,"r+")
                fo = open(file1, "w")
                fou = file_t.readlines()
                lno = int(entry4.get())
                n = 0
                for line in fou:
                    if lno == n+1:
                        print("found")
                        a = fou[n]
                        print(a)
                        st3 = a.split(" ")
                        st1=[]
                        for elem in st3:
                            st1.append(elem.strip())
                        print(st1)
                        for i in range(len(st1)):
                            if st1[i] == string1:
                                st1[i] = entry3.get()
                            else:
                                st1[i]=st1[i]
                        st2 = ""
                        for ele in st1:
                            st2+=ele+" "
                        st2+="\n"
                        print(st2)
                        fou[n] = st2
                        fo.write(fou[n])
                    else:
                        fo.write(fou[n])
                    n+=1
                fo.close()
                file_t.close()
            else:
                label2 = Label(newWindow2, text='Enter the replace string')
                label2.grid(column=0, row=19)
        button1 = Button(newWindow2,text='Replace', command=reply, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        button1.grid(column=0, row=18)

if __name__ == '__main__':
    window = Tk()
    window.title("FS Mini Project")
    window.geometry('400x250')
    l1 = Label(window, text="Menu")
    l1.grid(column=0, row=0)
    b1 = Button(window, text="1.To  get the files in which the strings are present  (Case Sensitive)",command=Text_search.txt_search)
    b1.grid(column=0, row=1)
    b2 = Button(window, text="2.To get files as well as line number of file  (Case Sensitive)",command=Text_search.txt_search_m)
    b2.grid(column=0, row=2)
    b3 = Button(window, text="3.To search in recusrive order (Case Sensitive)",command=Text_search.txt_search_r)
    b3.grid(column=0, row=3)
    b4 = Button(window, text="4.To  get the files in which the strings are present (Case insensitive)",command=Text_search.txt_search1)
    b4.grid(column=0, row=4)
    b5 = Button(window, text="5.To get files as well as line number of file (Case insensitive)",command=Text_search.txt_search_m1)
    b5.grid(column=0, row=5)
    b6 = Button(window, text="6.To search in recusrive order (Case insensitive)",command=Text_search.txt_search_r1)
    b6.grid(column=0, row=6)
    b7 = Button(window, text="7.Replace all the occerences of a string in a file",command=Text_search.replaceall)
    b7.grid(column=0, row=7)
    b8 = Button(window, text="8.Replace all the occerences of a string in a line in a file",command=Text_search.replaceocc)
    b8.grid(column=0, row=8)
    window.mainloop()
else:
    print("sorry, u r wrong")