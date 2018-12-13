import os;
import re;

search_path = input("Enter directory path to search : ")
file_type = input("File Extension (eg. .log or .txt) : ")
search_str = input("Enter the search string : ")

if not (search_path.endswith("/") or search_path.endswith("\\") ): 
    search_path = search_path + "/"

if not os.path.exists(search_path):
    search_path ="."

for fname in os.listdir(path=search_path):
    if fname.endswith(file_type):
        fo = open(search_path + fname, encoding='utf-8')
        line = fo.readline()
        line_no = 1
        # print(line_no)
        
        while line != '' :
            # print('I am the line' + search_str)
            index = line.find(search_str)
            if ( index != -1) :
                print(fname, "[", line_no, ",", index, "] ", line, sep="")
            
            line = fo.readline()
            line_no += 1
        
        fo.close()
