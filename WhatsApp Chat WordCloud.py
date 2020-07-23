# this is the main program that scans for all the files in the directory, determines if they are whatsapp chats 
# and then forms a worrdcloud for the viewer to analyse the overall sentiment of the conversation


from wordcloud  import WordCloud, STOPWORDS                             # importing Wordcloud to create wordcloud object and define stop words
from os.path    import isfile, join                                     # importing isFile and join to detect if the items in the directory are files                         
from os         import listdir                                          # importing listdir to list items in the directory

import matplotlib.pyplot as plt                                         # importing matplotliib to process wordcloud data into an image
import os                                                               # importing os to get current working direcotry


chatfile_names  =   list()                                              # empty files to append chat file names
mypath          =   os.getcwd()                                         # get current working direcotry path

print("\nCurrent Working Directory is",mypath)                          # print current working directory


for f in listdir(mypath):                                               # iterate through files in the current directory
    
    if isfile(join(mypath, f)):                                         # getting path of the file in the current directory
        
        if ".txt" and "WhatsApp Chat with" in f:                        # checking if they are WhatsApp chats
            
            chatfile_names.append(f)                                    # append file names to list


if "WhatsApp Chat with sample.txt" in chatfile_names:                   # checks if sample file has been appended and removes it
    
    chatfile_names.remove("WhatsApp Chat with sample.txt")

if len(chatfile_names)>0:                                               # checks if chats have been detected
    
    print("\nChats Files Detected\n",*chatfile_names,sep="\n")          # prints chats to screen

else:
    
    print("\nFailed to detect files\n")                                 # no chats have been found

for names in chatfile_names:                                            # iterates through all the chat files

    name_of_chat    =   names                                           # sets name to current chat
    
    print("\nworking on",name_of_chat)                                  # prints chat names
    
    colon1_pos  = None                                                  # detect position of colon to identify the position of the name string
    dash1_pos   = None                                                  # detect position of colon to identify the position of the name string
    names       = list()                                                # creating a an empty list to apprend names
    name1       = None                                                  # name of the first person
    name2       = None                                                  # name of the second person
    temp        = None                                                  # temporary variable

    f           = open("WhatsApp Chat with sample.txt",encoding="utf8") # opening sample whatsapp chat to detect names
    
    for line in f:                                                      # iteraties through all the lines

        reader  =   f.readline()                                        # assigns line to string

        if "end-to-end encryption. Tap for more info." in reader:       # skips app generated text
            
            continue

        if len(names)==2:                                               # skips loop when 2 names have been found
            
            break

        colon1_pos  =   reader.find(":",13)                             # assigns colon and dash position as name is located between these two in chat format
        dash1_pos   =   reader.find("-")
        temp        =   reader[dash1_pos:colon1_pos]

        if temp not in names and len(temp)>2:

            names.append(temp)                                          # appends name to string

    name1   =   names[0]                                                
    name2   =   names[1]

    print("\n",name1,"Person 1","\t",name2,"Person 2\n")                # prints the names of the individuals 
    f.close()                                                           # closes file to save memory

    iter_first_persons      =   0                                       # variable to count the number of lines for the first person 
    iter_second_person      =   0                                       # variable to count the number of lines for the second person 

    first_persons_message   =   name1                                   
    second_persons_message  =   name2

    first_persons_list      =   list()
    second_person_list      =   list()

    first_persons_string    =   ""                                      # string to contain all the words of the first person
    second_person_string    =   ""                                      # string to contain all the words of the second person

    def cloud(text,iter_val,message,wordcount):                         # function to draw word cloud

        wordcloud = WordCloud(width=1920, height=1080, margin=0).generate(text)     # Create the wordcloud object
        
        fig=plt.figure()                                                            # generate image:
        fig.suptitle(message+" "+str(iter_val)+" lines "+str(wordcount)+" Words")
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)
        
        try:
            if "." in message:
                message=message.replace('.','')
            fig.savefig(message)                                        # saving figure
            print("figure saved for",message)
        except:
            print("failed to save figure")                              # exception if file exists with the same name or if there are other errors

    with open(name_of_chat,encoding="utf8") as openfileobject:          # opening the specific file to generate the word cloud 
        
        for line in openfileobject:                                     # iterating through all the lines

            if "<Media omitted>" in line:                               # omitting lines where media files used to be
                
                continue
            
            if(first_persons_message in line):                          # for all the messages of the first person
                
                iter_first_persons+=1                                   # iterate the number of lines
                x=line.split(":")                                       # extracting the message part from the line
                first_persons_list.append(x[2])                         # appending the message to string
                first_persons_string=first_persons_string+x[2]+" "      # appending the string
            
            if(second_persons_message in line):                         # doing the same as above for the second person
                
                iter_second_person+=1
                y=line.split(":")
                second_person_list.append(y[2])
                second_person_string=second_person_string+y[2]+" "

    first_person_wordcount  = len(first_persons_string.split())         # counting the number of words for the first
    second_person_wordcount = len(second_person_string.split())         # and the second

    location=os.getcwd()                                                # get current working directory
    path=os.path.join(location, name_of_chat[:-4])                      # adding the name of the chat minus the extension to generate a folder 

    try:
        os.mkdir(path)                                                  # creating a folder with the name of the chat
        os.replace(os.path.join(location, name_of_chat),os.path.join(path, name_of_chat))   # changing path to enter into the chat folder
        os.chdir(path)                                                  # making the chat folder the current working directory

    except Exception as e:                                              # catching and printing any exceptions in creating the folder
        print(e)

    cloud(first_persons_string,iter_first_persons,first_persons_message,first_person_wordcount)     # calling the word cloud function for the first person
    cloud(second_person_string,iter_second_person,second_persons_message,second_person_wordcount)   # calling the word cloud function for the second person
    print("Chat wordcloud generation finished\n\n")                                                 # printing finished to indicate word cloud generation
    f.close()                                                                                       # closing open file to save memory
    os.chdir(mypath)                                                                                # changing directory back to the chat folder path

print("Program Ended Without Errors\nThis program was written by Anand Mahesh @manand881")          # this does what it does