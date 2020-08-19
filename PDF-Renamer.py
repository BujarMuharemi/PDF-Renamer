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

import PySimpleGUI as sg




#sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
'''
layout = [  [sg.Text('Wähle den PDF Ordner'),sg.Input(),sg.FolderBrowse()],                   
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text('Gefundene PDFs')] ,
            [sg.Listbox(values=(), size=(60, 6), key='-FILELIST-')] ]


# Create the Window
window = sg.Window('PDF-Renamer', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    window.Element("-FILELIST-").Update(values=['asdgggf','asdf','asdf'])


window.close()
'''

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
companyName="keinName"
billDate=""
billPrice=0.0


#looping threw all files
for file in files:       
        print("___Datei\t"+file)
        #cmd = pdt2textCMD+" "+pdfPath+pdfName
        jFix=r""+file
        newName =""
        #if(" " in pdfPath):
                #newName = j.replace(r" ",r"_")

#        os.rename(pdfPath+pdfName,pdfPath+newName)

        cmd = pdt2textCMD+r' "'+pdfPath+jFix+r'"'
              

        stream = os.popen(r""+cmd)
        output = stream.read()

        array=output.splitlines() # splitting the whole pdf by lines
        arrayCounter=0  #used to count, if a search failed

        dateFoundFlag=False
        nameFoundFlag=False

        priceList=[]


        #_looping threw each line
        for i in array: 
                # !delete 
                #print(i)
                #check if space is in line there                
                lineCheck = re.search("\s[R][0-9]*$",i)
                if(lineCheck):
                        lineCheck = re.split("\s",i)
                        #print(lineCheck[1])
                        #os.rename(r""+pdfPath+file,pdfPath+lineCheck[1]+".pdf")

                #x = re.search("^R+[G]*[0-9]+",i)
                #___


                 #__finding company name
                gmbhSearch = re.search("\s[G][m][bB][Hh]",i)     #searching for the GmbH string
                             
                if(gmbhSearch and not nameFoundFlag):                        
                        #print(i)       
                        companyName=""                 
                        justName=re.split("\s",i)       #splitting by spaces

                        for k in justName:      #adding the array elements together till GmbH appears
                                companyName+=k+" "
                                if("GmbH" in k):
                                        break

                        print("Name:\t"+companyName)   
                        nameFoundFlag=True                     
                        #break
                        ##os.rename(r""+pdfPath+j,pdfPath+i+".pdf")   
                else:
                        #print("no company name")                                             
                        arrayCounter+=1   
                
                #__finding date of the bill
                datumSearch_1 = re.search("[0-9]+[.]+[0-9]+[.]+[0-9]+",i)     
                datumSearch_2 = re.search("[0-9]+[-]+[0-9]+[-]+[0-9]+",i)     

                if((datumSearch_1 or datumSearch_2) and not dateFoundFlag):
                        justDate=re.split("\s",i)       #splitting by space, if some "Datum" etc is still there
                        if(len(justDate)>1):
                                billDate=justDate[1]
                        else:
                                billDate=justDate[0]

                        print("Datum:\t"+billDate)
                        dateFoundFlag=True
                        #print(justDate)
                        #break #remove to get all search results
                #else:   
                        #arrayCounter+=1
                        #print("kein Datum gefunden")

                #__finding price               
                priceSearch = re.search("^[0-9]+[,]+[0-9]+",i)   
                
                if(priceSearch):
                        priceList.append(i)
                        #print(i)

                #print(priceList)
                #map(float,priceList)
                floatPriceList=[0.0] #must have for usage of max() function               
                
                for price in priceList:
                        justPrice=re.split("\s",price) # splitting by spaces if EUR etc is there
                        #print(justPrice,end =" ")
                        #print(len(justPrice),end =" ")

                        #print(justPrice[0])
                        
                        #print(float(justPrice[0].replace(",",".")))
                        floatPriceList.append(float(justPrice[0].replace(",",".")))
                        #print(price)

                        #print(price, end=" ")
                        #print(type(price), end=" ")
                
                #print(max(floatPriceList))
                billPrice=max(floatPriceList)


        print("Preis:\t"+str(billPrice))
              

                
        #print(arrayCounter,len(array))
        
        #checking if there wasn't any company name found 
        if(arrayCounter==len(array)):
                #print("Kein Firmennamen gefunden")
                companyName="keinName"    
        
        
        print("Name:\t"+companyName+"\tDatum:\t"+billDate+"\tPreis:\t"+str(billPrice))
        fileName=r""+companyName+r"_"+billDate+r"_"+str(billPrice)
        print()
        os.rename(pdfPath+file,pdfPath+fileName+r".pdf")
        print("\n")


#input()
