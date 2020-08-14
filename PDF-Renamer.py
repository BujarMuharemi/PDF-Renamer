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
iban="_"

for j in files:
       

        #cmd = pdt2textCMD+" "+pdfPath+pdfName
        jFix=r""+j
        newName =""
        #if(" " in pdfPath):
                #newName = j.replace(r" ",r"_")

#        os.rename(pdfPath+pdfName,pdfPath+newName)


        cmd = pdt2textCMD+r' "'+pdfPath+jFix+r'"'
        print(">>>>>>> "+cmd)

        #a=os.system(cmd)

        stream = os.popen(r""+cmd)
        output = stream.read()

        array=output.splitlines()

        for i in array:               
                if(("Rechnung" or "RG") in i):
                        print(i)
                        iban = i
                        pdfName=j.split(".")[0]
                        #os.rename(pdfPath+pdfName+".pdf",pdfPath+pdfName+iban+".pdf")
                else:
                        iban = "-keineRechnung"
                        
       
        print(iban)
        #os.rename(pdfPath+pdfName,pdfPath+fileName+iban+".pdf")
       


#input()
