import os
import re
import sys
import argparse

class Text_search :
    def __init__(self, string2, i=None):
        self.path1= "C:/Users/ruthv/Desktop/FS/Records/"
        self.i=i
        if self.i:
            string3 = string2.lower()
            self.string1= string3
        else:
            self.string1=string2

    def txt_search(self):
        file_number = 0
        files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1+"/"+f)]
        for file in files:
            file_t = open(self.path1+"/"+file)
            file_text= file_t.read()
            if self.i:
                file_text=file_text.lower()
                file_t.close()
            if re.search(self.string1, file_text):
                print ("The text "+self.string1+" found in ", file)
        file_number=file_number+1
        print ("total files are ",file_number)
        Text_search.main()

    def txt_search_m(self):
        files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1+"/"+f)]
        file_number = 0
        for file in files:
            file_t = open(self.path1+"/"+file)
            line_number=1
            flag_file = 0
            for line1 in file_t:
                if self.i:
                    line1 = line1.lower()
                if re.search(self.string1, line1):
                    flag_file= 1
                    print ("The text "+self.string1+" found in ", file, " at line number ",line_number)
                line_number=line_number+1
            if flag_file == 1:
                file_number=file_number+1
                flag_file=0
            file_t.close()
        print ("total files are ",file_number)
        Text_search.main()

    def txt_search_r(self):
        file_number = 0
        for root, dir, files in os.walk(self.path1, topdown = True):
            files = [f for f in files if os.path.isfile(root+"/"+f)]
            file_number = 0
            for file in files:
                file= root+file
                file_t = open(file)
                line_number=1
                flag_file = 0
                for line1 in file_t:
                    if self.i:
                        line1=line1.lower()
                    if re.search(self.string1, line1):
                        flag_file= 1
                        print ("The text "+self.string1+" found in ", file, " at line number ",line_number)
                    line_number=line_number+1
            if flag_file == 1:
                file_number=file_number+1
                flag_file=0
            file_t.close()
        print ("total files are ",file_number)
        Text_search.main()

    def replaceall(self):
        path = "C:/Users/ruthv/Desktop/FS/Records/"
        dir_list = os.listdir(path)
        print("Files and directories in '", path, "' :")
        print(dir_list)
        file = input("Enter the the file name from the list\n")
        if file in dir_list:
            file = path+file
            file_t=open(file,"r")
            data = file_t.read()
            rtxt = input("Enter the text to be replaced with\n")
            data = data.replace(self.string1, rtxt)
            file_t.close
            file_t=open(file,"w")
            file_t.write(data)
            file_t.close()
            print("success")
            Text_search.main()
        else:
            print("Enter the proper filename")
            Text_search.main()

    def replaceocc(self):
        path = "C:/Users/ruthv/Desktop/FS/Records/"
        dir_list = os.listdir(path)
        print("Files and directories in '", path, "' :")
        print(dir_list)
        file = input("Enter the the file name from the list\n")
        if file in dir_list:
            file1 = path+"1"+file
            file = path+file
            file_t=open(file,"r+")
            fo = open(file1, "w")
            fou = file_t.readlines()
            lno = int(input("enter the line number\n"))
            n = 0
            for line in fou:
                if lno == n+1:
                    print("found")
                    a = fou[n]
                    print(a)
                    st1 = a.split(" ")
                    for i in range(len(st1)):
                        if st1[i] == self.string1:
                            st1[i] = input("enter the replacing string\n")
                    st2 = ""
                    for ele in st1:
                        st2+=ele+" "
                    print(st2)
                    fou[n] = st2
                    fo.write(fou[n])
                else:
                    fo.write(fou[n])
                n+=1
        fo.close()
        file_t.close()
        Text_search.main()

def main():
        parser = argparse.ArgumentParser(version='1.0')
        parser.add_argument('-m', nargs = 2, help = 'To get files as well as line number of files ')
        parser.add_argument('-s', nargs = 2, help = 'To get the files contain string ')
        parser.add_argument('-r', nargs = 2, help = 'To search in recusrive order ')
        parser.add_argument('-mi', nargs = 2, help = '-m option with case insensitive ')
        parser.add_argument('-si', nargs = 2, help = '-s option with case insensitive ')
        parser.add_argument('-ri', nargs = 2, help = '-r option with case insensitive ')
        args = parser.parse_args()
        try:
            if args.m:
                dir = args.m[1]
                obj1 = Text_search(args.m[0],dir)
                obj1.txt_search_m()
            elif args.s:
                if args.s[1]:
                    dir = args.s[1]
                    obj1 = Text_search(args.s[0],dir)
                    obj1.txt_search()
            elif args.r:
                if args.r[1]:
                    dir = args.r[1]
                    obj1 = Text_search(args.r[0],dir)
                    obj1.txt_search_r()
            elif args.mi:
                dir = args.mi[1]
                obj1 = Text_search(args.mi[0],dir,i=1)
                obj1.txt_search_m()
            elif args.si:
                if args.si[1]:
                    dir = args.si[1]
                    obj1 = Text_search(args.si[0],dir,i=1)
                    obj1.txt_search()
            elif args.ri:
                if args.ri[1]:
                    dir = args.ri[1]
                    obj1 = Text_search(args.ri[0],dir,i=1)
                    obj1.txt_search_r()
        except Exception as e:
                print (e)
                print ("Please use proper form to search a file use following instructions")
                print ("see file-name")
                print ("Use <see -h > For help")
main()











