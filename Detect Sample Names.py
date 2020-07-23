# this program has been purposed to find the names of the individuals in a chat.
# this program works with only two people and not more than that.


colon1_pos  = None                                                  # detect position of colon to identify the position of the name string
dash1_pos   = None                                                  # detect position of colon to identify the position of the name string
names       = list()                                                # creating a an empty list to apprend names
name1       = None                                                  # name of the first person
name2       = None                                                  # name of the second person
temp        = None                                                  # temporary variable

f           = open("WhatsApp Chat with sample.txt",encoding="utf8") # opening sample whatsapp chat to detect names

for line in f:

    reader=f.readline()                                             # assigning the line read to a variable

    if "end-to-end encryption. Tap for more info." in reader:       # skipping the unnecessary 
        
        continue

    if len(names)==2:                                               # ending the loop once the two names have been found                                        
        
        break

    colon1_pos=reader.find(":",13)                                  # names in whatsapp chats are inbetween a - & :
    dash1_pos=reader.find("-")
    temp=reader[dash1_pos:colon1_pos]                               # appending the name string to the temp variable
    
    if temp not in names and len(temp)>2:                           # if name isnt in the list and is longer than 2 chars then append
        
        names.append(temp)


name1=names[0]
name2=names[1]
print(name1,name2)                                          