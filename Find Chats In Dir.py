# This program exists to detecct WhatsApp Chats in the directory of the program.


from    os.path import isfile, join     # importing isFile and join to detect if the items in the directory are files 
from    os      import listdir          # importing listdir to list items in the directory
import  os                              # importing os to get current working direcotry


chatfile_names  =   list()              # empty files to append chat file names
mypath          =   os.getcwd()         # get current working direcotry path


for f in listdir(mypath):               # iterate through files in the current directory
    
    if isfile(join(mypath, f)):         # getting path of the file in the current directory
        
        if ".txt" and "WhatsApp"in f:   # checking if they are WhatsApp chats
            
            chatfile_names.append(f)    # append file names to list


print("\n",chatfile_names)              # as it says