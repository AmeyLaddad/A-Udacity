import urllib

def read_text():
    file = open("/home/hp/Desktop/About Briquttes and machine.txt")
    Data_file = file.read()
    print (Data_file)
    file.close()    
    check_profanity(Data_file)

def check_profanity(text):
    c = urllib.urlopen("http://www.wdyl.com/profanity?q"+text)
    #http://isithackday.com/arrpi.php?text also can be used
    #print (c.read())
    if "true" in c.read():
        print("Alert !!!")
    elif "false" in c.read():
        print ("No CURSE words")
    else:
        print ("Error in reading file !!!")        
        
    c.close()
    
read_text()
