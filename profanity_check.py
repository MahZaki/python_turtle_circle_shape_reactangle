import urllib
import time
def read_text():
	text = open("C:\\Users\\DELL\\Downloads\\Documents\\test.txt")
	read_text = text.read()
	#print [(read_text)]
	text.close()
	check_profanity(read_text)
	
def check_profanity(text):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text="+text)
    output = connection.read()
    connection.close
    print("Checking ... " )
    time.sleep(1)
    if "true" in output:
        print("Profanity Alert !")
    elif "false" :
        print ("This document has no curse words !")
    else :
        print("Could not scan the document properly ")
read_text()
