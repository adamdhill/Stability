#Dot delimited, which separates Parts and Sections. 
#Delete the "." in re.split in order to get point citations on highly altered sections

import os, re, sys
os.chdir('/Users/[...]') #Change where relevant 

label = "[...].txt" #file containing regs
contents = open(label, "r")
string = contents.read()
def text(label):
     file = open(label, "r")
     string = file.read()
     text = re.split(r"(\s+|[,:;.\"()/&]|[?!]+|-{2,})",string)
     return text

from collections import Counter 
Counter(text(label))
a = Counter(text(label))

#Print to text file, where "a" is a = Counter(inputText(filename))

#output = open('Out.txt', 'w')
#output.write(str(a))
#output.close()
