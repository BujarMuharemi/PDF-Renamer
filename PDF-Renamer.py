'''
PDF RENAMER

TO_DO
-should have a UI so u can choose in which folder it should run threw
-check if it finds an RN, if not exception, error etc->rename file....
-query for Rechnungen should be checked again
-write some methods, so the code is cleaner->follow guidlines
'''


import os
from os import listdir
from os.path import isfile, join
import re 


def getFiles(path):
        return [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".pdf")]


pdfPath = r'D:/Documents/_DEVELOPMENT/Projects/Reifenhandel/PDF-Renamer/pdfs/'
fileName = r"qwert"
pdfName = fileName+r".pdf"
pdt2textCMD = r"python C:\Users\Bujar\AppData\Local\Programs\Python\Python38-32\Scripts\pdf2txt.py"
iban = ""

#example cmd
cmd = r"python C:\Users\Resul\AppData\Local\Programs\Python\Python37-32\Scripts\pdf2txt.py C:\Users\Resul\Desktop\test3\1234.pdf"

#print(getFiles(pdfPath))

files = getFiles(pdfPath)


#looping threw all files
for j in files:       
        
        #cmd = pdt2textCMD+" "+pdfPath+pdfName
        jFix=r""+j
        newName =""
        #if(" " in pdfPath):
                #newName = j.replace(r" ",r"_")

#        os.rename(pdfPath+pdfName,pdfPath+newName)

        cmd = pdt2textCMD+r' "'+pdfPath+jFix+r'"'
              

        stream = os.popen(r""+cmd)
        output = stream.read()

        array=output.splitlines() # splitting the whole pdf by lines

        #looping threw each line
        for i in array: 

                #check if space is in line there                
                lineCheck = re.search("\s[R][0-9]*$",i)
                if(lineCheck):
                        lineCheck = re.split("\s",i)
                        print(lineCheck[1])
                        os.rename(r""+pdfPath+j,pdfPath+lineCheck[1]+".pdf")


                x = re.search("^R+[G]*[0-9]+",i)
                if(x):                        
                        print(i)
                        os.rename(r""+pdfPath+j,pdfPath+i+".pdf")                       
                        
               
        #os.rename(pdfPath+pdfName,pdfPath+fileName+iban+".pdf")
       


#input()
