##Soroush Hajizadeh Rosalind problem MPRT http://rosalind.info/problems/mprt/
#Pretty simple, done Oct 2018
import urllib
import urllib2

list = open('list.txt', 'r') #fetch from rosalind list
url = ""
for x in list:
    url = "" + "https://www.uniprot.org/uniprot/" + x.strip("\n") + ".fasta"  #Make proper webpage and Fetch from web page the sequence an


    the_page = (urllib2.urlopen(url)).read() #actually fetches it
    count = 0
    fullString = ""
    name = x.strip("\n") #remove new lines from text
    for line in the_page:

        if(line == "\n"): # this way we create the text only from the actual sequence
            count = count+1
            continue
        if (count > 0):
            fullString += line

    position = 0
    found = 0
    for x in fullString: #now that we have the string we can check to see if it fits our condition
        if (fullString[position] == "N"):
            if (fullString[position+1] != "P"):
                if (fullString[position+2] == "S" or fullString[position+2] ==  "T"):
                    if (fullString[position+3] != "P"):
                        if (found == 0):
                            print name
                        found = found +1
                        print (position+1),
                    #    print fullString[position:(position+4)]

        position = position+1
        if (position == len(fullString)-3):
            break
    if(found !=0): #We only make a new line if one is found, else we don't need to
        print ("\n"),
    #print fullString
